const fs = require('fs-extra');

const imageTypes = ['PNG', 'GIF', 'BMP', 'JPEG', 'TIFF'];
const videoTypes = ['AVI', 'MP4', 'MOV', 'MKV', 'WEBM', 'OGV'];
const soundTypes = ['OGG', 'WAV', 'MP3', 'FLAC'];

const read = async (path, offset, length) => {
    const fp = await fs.open(path);
    const buff = Buffer.alloc(length);
    
    await fs.read(fd, buff, 0, length, offset);
    await fs.close();

    return buff;
};


const parser = {

    PNG: async (path, result) => {
        const buff = await read(path, 18, 6);
        result.width = buff.readUInt16BE(0);
        result.height = buff.readUInt16BE(4);
    },

    GIF: async (path, result) => {
        const buff = await read(path, 6, 4);
        result.width = buff.readUInt16LE(0);
        result.height = buff.readUInt16LE(2);
    },

    BMP: async (path, result) => {
        const buff = await read(path, 18, 8);
        result.width = buff.readUInt32LE(0);
        result.height = buff.readUInt32LE(4);
    },

    JPEG: async (path, result) => {
        const sof = [0xc0, 0xc1, 0xc2, 0xc3, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xcf, 0xde];
        const buff = await read(path, 2, 64000);
        
        let pos = 0;

        while (buff[pos++] == 0xff) {
            let marker = buff[pos++];
            let size = buff.readUInt16BE(pos);

            if (marker == 0xda) break;

            if (sof.includes(marker)) {
                result.height = buff.readUInt16BE(pos + 3);
                result.width = buff.readUInt16BE(pos + 5);
                break;
            }

            pos += size;
        }
    },

    TIFF: async (path, result) => {
        const buff = await read(path, 0, 64000);
        const le = buff.toString('ascii', 0, 2) == 'II';
        let pos = 0;
        const readUInt16 = () => { pos += 2; return buff[le ? 'readUInt16LE' : 'readUInt16BE'](pos - 2); }
        const readUInt32 = () => { pos += 4; return buff[le ? 'readUInt32LE' : 'readUInt32BE'](pos - 4); }

        let offset = readUInt32();
        
        while (pos < buff.length && offset > 0) {
            let entries = readUInt16(offset);
            let start = pos;

            for (let i = 0; i < entries; i++) {
                let tag = readUInt16();
                let type = readUInt16();
                let length = readUInt32();
                let data = (type == 3) ? readUInt16() : readUInt32();
                if (type == 3) pos += 2;

                if (tag == 256) {
                    result.width = data;
                } else if (tag == 257) {
                    result.height = data;
                }

                if (result.width > 0 && result.height > 0) {
                    return;
                }
            }

            offset = readUInt32();
            pos += offset;
        }
    },

    AVI: async (path, result) => {
        const buff = await read(path, 0, 144);
        result.width = buff.readUInt32LE(64);
        result.height = buff.readUInt32LE(68);
        result.duration = ~~(buff.readUInt32LE(128) / buff.readUInt32LE(132) * buff.readUInt32LE(140));
    },

    MP4: async (path, result) => {
        return parser.MOV(path, result);
    },

    MOV: async (path, result, pos = 0) => {
        const buff = await read(path, 0, 64000);

        while (pos < buff.length) {
            let size = buff.readUInt32BE(pos);
            let name = buff.toString('ascii', pos + 4, 4);

            if (name == 'mvhd') {
                let scale = buff.readUInt32BE(pos + 20);
                let duration = buff.readUInt32BE(pos + 24);
                result.duration = ~~(duration / scale);
            }

            if (name == 'tkhd') {
                let m0 = buff.readUInt32BE(pos + 48);
                let m4 = buff.readUInt32BE(pos + 64);
                let w = buff.readUInt32BE(pos + 84);
                let h = buff.readUInt32BE(pos + 88);
                if (w > 0 && h > 0) {
                    result.width = w / m0;
                    result.height = h / m4;
                    return;
                }
            }

            if (name == 'moov' || name == 'trak') {
                await parser.MOV(path, pos + 8);
            }

            pos += size;
        }
    },

    WEBM: async (path, result) => {
        return parser.EBML(path, result);
    },

    MKV: async (path, result) => {
        return parser.EBML(path, result);
    },

    EBML: async (path, result) => {
        const containers = ['\x1a\x45\xdf\xa3', '\x18\x53\x80\x67', '\x15\x49\xa9\x66', '\x16\x54\xae\x6b', '\xae', '\xe0'];
        const buff = await read(path, 0, 64000);

        // TODO parse EBML
    },

    OGV: async (path, result) => {
        return parser.OGG(path, result);
    },

    OGG: async (path, result) => {
        const buff = await read(apth, 0, 64000);
        let pos = 0, vorbis;

        while (buff.toString('ascii', pos, pos + 4) == 'OggS') {
            let version = buff[pos + 4];
            let b = buff[pos + 5];
            let continuation = !!(b & 0x01);
            let bos = !!(b & 0x02);
            let eos = !!(b & 0x04);
            let position = Number(buff.readBigUInt64LE(pos + 6));
            let serial = buff.readUInt32LE(pos + 14);
            let pageNumber = buff.readUInt32LE(pos + 18);
            let checksum = buff.readUInt32LE(pos + 22);
            let pageSegments = buff[path + 26];
            let lacing = buff.slice(pos + 27, pos + 27 + pageSegments);
            let pageSize = lacing.reduce((p, v) => p + v, 0);
            let start = pos + 27 + pageSegments;
            let pageHeader = buff.slice(start, start + 7);

            if (pageHeader.compare(Buffer.from([0x01, 'v', 'o', 'r', 'b', 'i', 's']))) {
                vorbis = { serial, sampleRate: buff.readUInt32LE(start + 12) };
            }

            if (pageHeader.compare(Buffer.from([0x80, 't', 'h', 'e', 'o', 'r', 'a']))) {
                let version = buff.slice(start + 7, start + 10);
                result.width = buff.readUInt16BE(start + 10) << 4;
                result.height = buff.readUInt16BE(start + 12) << 4;

                if (version >= 0x030200) {
                    let width = buff.slice(start + 14, start + 17);
                    let height = buff.slice(start + 17, start + 20);

                    if (width <= result.width && width > result.width - 16 && height <= result.height && height > result.height - 16) {
                        result.width = width;
                        result.height = height;
                    }
                }
            }

            if (eos && vorbis && serail == vorbis.serial) {
                result.duration = ~~(position / vorbis.sampleRate);
            }

            pos = start + pageSize;
        }
    },

    WAV: async (path, result) => {
        const buff = await read(path, 0, 32);
        let size = buff.readUInt32LE(4);
        let rate = buff.readUInt32LE(28);
        result.duration = ~~(size / rate);
    },

    MP3: async (path, result) => {
        const versions = [2.5, 0, 2, 1];
        const layers = [0, 3, 2, 1];
        const bitrates = [
            [ // version 2.5
                [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], // reserved
                [0, 8,16,24, 32, 40, 48, 56, 64, 80, 96,112,128,144,160], // layer 3
                [0, 8,16,24, 32, 40, 48, 56, 64, 80, 96,112,128,144,160], // layer 2
                [0,32,48,56, 64, 80, 96,112,128,144,160,176,192,224,256]  // layer 1
            ],
            [ // reserved
                [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], // reserved
                [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], // reserved
                [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], // reserved
                [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]  // reserved
            ],
            [ // version 2
                [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], // reserved
                [0, 8,16,24, 32, 40, 48, 56, 64, 80, 96,112,128,144,160], // layer 3
                [0, 8,16,24, 32, 40, 48, 56, 64, 80, 96,112,128,144,160], // layer 2
                [0,32,48,56, 64, 80, 96,112,128,144,160,176,192,224,256]  // layer 1
            ],
            [ // version 1
                [0, 0, 0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0], // reserved
                [0,32,40,48, 56, 64, 80, 96,112,128,160,192,224,256,320], // layer 3
                [0,32,48,56, 64, 80, 96,112,128,160,192,224,256,320,384], // layer 2
                [0,32,64,96,128,160,192,224,256,288,320,352,384,416,448]  // layer 1
            ]
        ]
        const srates = [
            [11025, 12000,  8000, 0], // mpeg 2.5
            [    0,     0,     0, 0], // reserved
            [22050, 24000, 16000, 0], // mpeg 2
            [44100, 48000, 32000, 0]  // mpeg 1
        ]
        const tsamples = [
            [0,  576, 1152, 384], // mpeg 2.5
            [0,    0,    0,   0], // reserved
            [0,  576, 1152, 384], // mpeg 2
            [0, 1152, 1152, 384]  // mpeg 1
        ];
        const slotSizes = [0, 1, 1, 4];
        const modes = ['stereo', 'joint_stereo', 'dual_channel', 'mono'];
        const buff = await read(path, 0, 64000);

        let duration = 0;
        let count = 0;
        let skip = 0;
        let pos = 0;

        while (pos < buff.length) {
            let start = pos;

            if (buff.toString('ascii', pos, 4) == 'TAG+') {
                skip += 227;
                pos += 227;
            } else if (buff.toString('ascii', pos, 3) == 'TAG') {
                skip += 128;
                pos += 128;
            } else if (buff.toString('ascii', pos, 3) == 'ID3') {
                let bytes = buff.readUInt32BE(pos + 6);
                let size = 10 + (bytes[0] << 21 | bytes[1] << 14 | bytes[2] << 7 | bytes[3]);
                skip += size;
                pos += size;
            } else {
                let hdr = buff.slice(pos, pos + 4);

                while (pos < buff.length && !(hdr[0] == 0xff && (hdr[1] & 0xe0) == 0xe0)) {
                    pos++;
                    hdr = buff.slice(pos, pos + 4);
                }

                let ver = (hdr[1] & 0x18) >> 3;
                let lyr = (hdr[1] & 0x06) >> 1;
                let pad = (hdr[2] & 0x02) >> 1;
                let brx = (hdr[2] & 0xf0) >> 4;
                let srx = (hdr[2] & 0x0c) >> 2;
                let mdx = (hdr[3] & 0xc0) >> 6;

                let version = versions[ver];
                let layer = layers[lyr];
                let bitrate = bitrates[ver][lyr][brx] * 1000;
                let samprate = srates[ver][srx];
                let samples = tsamples[ver][lyr];
                let slotSize = slotSizes[lyr];
                let mode = modes[mdx];
                let fsize = ~~(((samples / 8 * bitrate) / samprate) + (pad ? slotSize : 0));

                count++;

                if (count == 1) {
                    if (layer != 3) {
                        pos += 2;
                    } else {
                        if (mode != 'mono') {
                            if (version == 1) {
                                pos += 32;
                            } else {
                                pos += 17;
                            }
                        } else {
                            if (version == 1) {
                                pos += 17;
                            } else {
                                pos += 9;
                            }
                        }
                    }

                    if (buff.toString('ascii', pos, pos + 4) == 'Xing' && (buff.readUInt32BE(pos + 4) & 0x0001) == 0x0001) {
                        let totalFrames = buff.readUInt32BE(pos + 8);
                        duration = totalFrames * samples / samprate;
                        break;
                    }
                }

                if (fsize < 1) break;

                pos = start + fsize;

                duration += (samples / samprate);
            }
        }
        
        result.duration = ~~duration;
    },

    FLAC: async (path, result) => {
        const buff = await read(path, 18, 8);
        let rate = (buff[0] << 12) | (buff[1] << 4) | ((buff[2] & 0xf0) >> 4);
        let size = ((buff[3] & 0x0f) << 32) | (buff[4] << 24) | (buff[5] << 16) | (buff[6] << 8) | buff[7];
        result.duration = ~~(size / rate);
    },

};

async function detect(path) {
    const buff = await read(path, 0, 12);

    if (buff.slice(0, 8).compare(Buffer.from([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a]))) {
        return 'PNG';
    }

    if (buff.toString('ascii', 0, 3) == 'GIF') {
        return 'GIF';
    }

    if (buff.toString('ascii', 0, 2) == 'BM') {
        return 'BMP';
    }

    if (buff.slice(0, 2).compare(Buffer.from([0xff, 0xd8]))) {
        return 'JPEG';
    }

    if (buff.toString('ascii', 0, 2) == 'II' && buff.readUInt16LE(2) == 42) {
        return 'TIFF';
    }

    if (buff.toString('ascii', 0, 2) == 'MM' && buff.readUInt16BE(2) == 42) {
        return 'TIFF';
    }

    if (buff.toString('ascii', 0, 4) == 'RIFF' && buff.toString('ascii', 8, 4) == 'AVI ') {
        return 'AVI';
    }

    if (buff.toString('ascii', 4, 4) == 'ftyp') {
        return 'MP4';
    }

    if (buff.toString('ascii', 4, 4) == 'moov') {
        return 'MOV';
    }

    if (buff.slice(0, 4).compare(Buffer.from([0x1a, 0x45, 0xdf, 0xa3]))) {
        // TODO detect MKV

        return 'EBML';
    }

    if (buff.toString('ascii', 0, 4) == 'OggS') {
        // TODO detect OGV
        
        return 'OGG'
    }

    if (buff.toString('ascii', 0, 4) == 'RIFF', buff.toString('ascii', 8, 4) == 'WAVE') {
        return 'WAV';
    }

    if (buff.toString('ascii', 0, 3) == 'ID3' || (buf[0] == 0xff && (buff[1] & 0xe0))) {
        return 'MP3';
    }

    if (buff.toString('ascii', 0, 4) == 'fLaC') {
        return 'FLAC';
    }

    return null
}

module.exports = {

    detect: async function(options) {
        let path = this.parseRequired(options.path, 'string', 'metadata.detect: path is required.');

        return detect(path);
    },

    isImage: async function(options) {
        let path = this.parseRequired(options.path, 'string', 'metadata.isImage: path is required.');
        let type = await detect(path);
        let cond = imageTypes.includes(type);
        
        if (cond) {
            if (options.then) {
                await this.exec(options.then, true);
            }
        } else if (options.else) {
            await this.exec(options.else, true);
        }

        return cond;
    },

    isVideo: async function(options) {
        let path = this.parseRequired(options.path, 'string', 'metadata.isVideo: path is required.');
        let type = await detect(path);
        let cond = videoTypes.includes(type);
        
        if (cond) {
            if (options.then) {
                await this.exec(options.then, true);
            }
        } else if (options.else) {
            await this.exec(options.else, true);
        }

        return cond;
    },

    isSound: async function(options) {
        let path = this.parseRequired(options.path, 'string', 'metadata.isSound: path is required.');
        let type = await detect(path);
        let cond = soundTypes.includes(type);
        
        if (cond) {
            if (options.then) {
                await this.exec(options.then, true);
            }
        } else if (options.else) {
            await this.exec(options.else, true);
        }

        return cond;
    },

    fileinfo: async function(options) {
        let path = this.parseRequired(options.path, 'string', 'metadata.fileinfo: path is required.');
        let type = await detect(path);
        let result = { type, width: null, height: null, duration: null };

        if (parser[type]) {
            await parser[type](path, result);
        }

        return result;
    },

};