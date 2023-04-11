const fs = require('fs-extra');
const Sharp = require('sharp');
const debug = require('debug')('server-connect:image');
const { basename, extname, join } = require('path');
const { toAppPath, toSystemPath, parseTemplate, getUniqFile } = require('../core/path');

const positions = {
    'center': 0,
    'centre': 0,
    'top': 1,
    'north': 1,
    'right': 2,
    'east': 2,
    'bottom': 3,
    'south': 3,
    'left': 4,
    'west': 4,
    'top right': 5,
    'right top': 5,
    'northeast': 5,
    'bottom right': 6,
    'right bottom': 6,
    'southeast': 6,
    'bottom left': 7,
    'left bottom': 7,
    'southwest': 7,
    'top left': 8,
    'left top': 8,
    'northwest': 8,
    'entropy': 16,
    'attention': 17
};

function cw(w, meta) {
    if (typeof w == 'string') {
        if (/%$/.test(w)) {
            w = meta.width * parseFloat(w) / 100;
        }
    }

    if (w < 0) {
        w = meta.width + w;
    }

    return parseInt(w);
}

function ch(h, meta) {
    if (typeof h == 'string') {
        if (/%$/.test(h)) {
            h = meta.height * parseFloat(h) / 100;
        }
    }

    if (h < 0) {
        h = meta.height + h;
    }

    return parseInt(h);
}

function cx(x, w, meta) {
    if (typeof x == 'string') {
        switch (x) {
            case 'left':
                x = 0;
                break;
            case 'center':
                x = (meta.width - w) / 2;
                break;
            case 'right':
                x = meta.width - w;
                break;
            default:
                if (/%$/.test(x)) {
                    x = (meta.width - w) * parseFloat(x) / 100;
                }
        }
    }

    if (x < 0) {
        x = meta.width - w + x;
    }

    return parseInt(x);
}

function cy(y, h, meta) {
    if (typeof y == 'string') {
        switch (y) {
            case 'top':
                y = 0;
                break;
            case 'middle':
                y = (meta.height - h) / 2;
                break;
            case 'bottom':
                y = meta.height - h;
                break;
            default:
                if (/%$/.test(y)) {
                    y = (meta.height - h) * parseFloat(y) / 100;
                }
        }
    }

    if (y < 0) {
        y = meta.height - h + y;
    }

    return parseInt(y);
}

async function updateImage(sharp) {
    sharp.image = Sharp(await sharp.image.toBuffer());
    sharp.metadata = await sharp.image.metadata();
}

module.exports = {

    getImageSize: async function (options) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'image.getImageSize: path is required.'));

        const image = Sharp(path);
        const metadata = await image.metadata();

        return {
            width: metadata.width,
            height: metadata.height
        };
    },

    load: async function (options, name) {
        let path = toSystemPath(this.parseRequired(options.path, 'string', 'image.load: path is required.'));
        let orient = this.parseOptional(options.autoOrient, 'boolean', false);

        this.req.image = this.req.image || {};
        this.req.image[name] = { name: basename(path), image: Sharp(path), metadata: null };

        const sharp = this.req.image[name];
        if (orient) sharp.image.rotate();

        await updateImage(sharp);

        return {
            name: basename(path),
            width: sharp.metadata.width,
            height: sharp.metadata.height
        };
    },

    save: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.save: instance "${options.instance} doesn't exist.`);

        let path = toSystemPath(this.parseRequired(options.path, 'string', 'image.save: path is required.'));
        let format = this.parseOptional(options.format, 'string', 'jpeg').toLowerCase();
        let template = this.parseOptional(options.template, 'string', '{name}{ext}');
        let overwrite = this.parseOptional(options.overwrite, 'boolean', false);
        let createPath = this.parseOptional(options.createPath, 'boolean', true);
        let background = this.parseOptional(options.background, 'string', '#FFFFFF');
        let quality = this.parseOptional(options.quality, 'number', 75);

        if (!fs.existsSync(path)) {
            if (createPath) {
                await fs.ensureDir(path);
            } else {
                throw new Error(`image.save: path "${path}" doesn't exist.`);
            }
        }

        let file = join(path, sharp.name);

        if (template) {
            file = parseTemplate(file, template);
        }

        if (format == 'auto') {
            switch (extname(file).toLowerCase()) {
                case '.png': format = 'png'; break;
                case '.gif': format = 'gif'; break;
                case '.webp': format = 'webp'; break;
                default: format = 'jpeg';
            }
        }
        
        if (format == 'jpeg') {
            sharp.image.flatten({ background });
            sharp.image.toFormat(format, { quality });
        } else if (format == 'webp') {
            sharp.image.toFormat(format, { quality });
        } else {
            sharp.image.toFormat(format);
        }

        const data = await sharp.image.toBuffer();
        
        file = file.replace(extname(file), '.' + format.replace('jpeg', 'jpg'));
        
        if (fs.existsSync(file)) {
            if (overwrite) {
                await fs.unlink(file);
            } else {
                file = getUniqFile(file);
            }
        }

        await fs.writeFile(file, data) //.toFile(file);

        return toAppPath(file);
    },

    resize: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.resize: instance "${options.instance} doesn't exist.`);

        let width = this.parseOptional(cw(this.parse(options.width), sharp.metadata), 'number', null);
        let height = this.parseOptional(ch(this.parse(options.height), sharp.metadata), 'number', null);
        let upscale = this.parseOptional(options.upscale, 'boolean', false);

        if (isNaN(width)) width = null;
        if (isNaN(height)) height = null;

        sharp.image.resize(width, height, { fit: width && height ? 'fill' : 'cover', withoutEnlargement: !upscale });

        await updateImage(sharp);
    },

    crop: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.crop: instance "${options.instance} doesn't exist.`);

        let width = this.parseRequired(cw(this.parse(options.width)), 'number', 'image.crop: width is required.');
        let height = this.parseRequired(ch(this.parse(options.height)), 'number', 'image.crop: height is required.');
        if (width > sharp.metadata.width) width = sharp.metadata.width;
        if (height > sharp.metadata.height) height = sharp.metadata.height;
        let left = this.parseRequired(cx(this.parse(options.x), width, sharp.metadata), 'number', 'image.crop: x is required.');
        let top = this.parseRequired(cy(this.parse(options.y), height, sharp.metadata), 'number', 'image.crop: y is required.');

        sharp.image.extract({ left, top, width, height });
        
        await updateImage(sharp);
    },

    cover: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.cover: instance "${options.instance}" doesn't exist.`);

        let width = this.parseRequired(options.width, 'number', 'image.cover: width is required.');
        let height = this.parseRequired(options.height, 'number', 'image.cover: height is required.');
        // position: see positions object for options
        let position = this.parseOptional(options.position, 'string', 'center');
        // kernel: 'nearest', 'cubic', 'mitchell', 'lanczos2', 'lanczos3'
        let kernel = this.parseOptional(options.kernel, 'string', 'lanczos3');

        position = positions[position] || 0;

        sharp.image.resize({ width, height, position, kernel });
        
        await updateImage(sharp);
    },

    watermark: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.watermark: instance "${options.instance} doesn't exist.`);

        let path = toSystemPath(this.parseRequired(options.path, 'string', 'image.watermark: path is required.'));
        let image = Sharp(path);
        let metadata = await image.metadata();
        let input = await image.toBuffer();
        let left = this.parseRequired(cx(this.parse(options.x), metadata.width, sharp.metadata), 'number', 'image.watermark: x is required.');
        let top = this.parseRequired(cy(this.parse(options.y), metadata.height, sharp.metadata), 'number', 'image.watermark: y is required.');

        sharp.image.composite([{ input, left, top }]);
    },

    text: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.text: instance "${options.instance} doesn't exist.`);

        let x = this.parse(options.x);
        let y = this.parse(options.y);
        let text = this.parseRequired(options.text, 'string', 'image.text: text is required.');
        let font = this.parseOptional(options.font, 'string', 'Verdana');
        let size = this.parseOptional(options.size, 'number', 24);
        let color = this.parseOptional(options.color, 'string', '#ffffff');

        let width = sharp.metadata.width;
        let height = sharp.metadata.height;
        let anchor = 'start';

        switch (x) {
            case 'left':
                x = '0%';
                anchor = 'start';
                break;
            case 'center':
                x = '50%';
                anchor = 'middle';
                break;
            case 'right':
                x = '100%';
                anchor = 'end';
                break;
            default:
                if (x < 0) {
                    x = width - x;
                    anchor = 'end';
                }
        }

        switch (y) {
            case 'top':
                y = size;
                break;
            case 'middle':
                y = (height / 2) - (size / 2);
                break;
            case 'bottom':
                y = height;
                break;
            default:
                if (y < 0) {
                    y = height - size - y;
                }
        }

        let svg = `
            <svg width="${width}" height="${height}">
                <style>
                    .text {
                        fill: ${color};
                        font-family: "${font}";
                        font-size: ${size}px;
                        line-height: 1;
                    }
                </style>
                <text x="${x}" y="${y}" text-anchor="${anchor}" class="text">${text}</text>
            </svg>
        `;

        const input = await Sharp(Buffer.from(svg)).toBuffer();

        sharp.image.composite([{ input, left: 0, top: 0 }]);
    },

    tiled: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.tiled: instance "${options.instance} doesn't exist.`);

        let input = toSystemPath(this.parseRequired(options.path, 'string', 'image.tiled: path is required.'));
        let padding = this.parseOptional(options.padding, 'number', 0);

        if (padding) {
            input = await Sharp(input).extend({
                top: padding, left: padding, bottom: 0, right: 0, background: { r: 0, g: 0, b: 0, alpha: 0 }
            }).toBuffer();
        }

        sharp.image.composite([{ input, left: 0, top: 0, tile: true }]);
    },

    flip: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.flip: instance "${options.instance} doesn't exist.`);

        let horizontal = this.parseOptional(options.horizontal, 'boolean', false);
        let vertical = this.parseOptional(options.vertical, 'boolean', false);

        if (horizontal) sharp.image.flop();
        if (vertical) sharp.image.flip();
    },

    rotateLeft: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.rotateLeft: instance "${options.instance} doesn't exist.`);

        sharp.image.rotate(-90);

        await updateImage(sharp);
    },

    rotateRight: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.rotateRight: instance "${options.instance} doesn't exist.`);

        sharp.image.rotate(90);

        await updateImage(sharp);
    },

    smooth: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.smooth: instance "${options.instance} doesn't exist.`);

        sharp.image.convolve({
            width: 3,
            height: 3,
            kernel: [
                1, 1, 1,
                1, 1, 1,
                1, 1, 1
            ]
        });
    },

    blur: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.blur: instance "${options.instance} doesn't exist.`);

        sharp.image.convolve({
            width: 3,
            height: 3,
            kernel: [
                1, 2, 1,
                2, 4, 2,
                1, 2, 1
            ]
        });
    },

    sharpen: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.sharpen: instance "${options.instance} doesn't exist.`);

        sharp.image.convolve({
            width: 3,
            height: 3,
            kernel: [
                0, -2, 0,
                -2, 15, -2,
                0, -2, 0
            ]
        });
    },

    meanRemoval: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.meanRemoval: instance "${options.instance} doesn't exist.`);

        sharp.image.convolve({
            width: 3,
            height: 3,
            kernel: [
                -1, -1, -1,
                -1, 9, -1,
                -1, -1, -1
            ]
        });
    },

    emboss: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.emboss: instance "${options.instance} doesn't exist.`);

        sharp.image.convolve({
            width: 3,
            height: 3,
            kernel: [
                -1, 0, -1,
                0, 4, 0,
                -1, 0, -1
            ],
            offset: 127
        });
    },

    edgeDetect: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.edgeDetect: instance "${options.instance} doesn't exist.`);

        sharp.image.convolve({
            width: 3,
            height: 3,
            kernel: [
                -1, -1, -1,
                0, 0, 0,
                1, 1, 1
            ],
            offset: 127
        });
    },

    grayscale: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.grayscale: instance "${options.instance} doesn't exist.`);

        sharp.image.grayscale();
    },

    sepia: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.sepia: instance "${options.instance} doesn't exist.`);

        sharp.image.tint({ r: 112, g: 66, b: 20 });
    },

    invert: async function (options) {
        const sharp = this.req.image[options.instance];
        if (!sharp) throw new Error(`image.invert: instance "${options.instance} doesn't exist.`);

        sharp.image.negate();
    },

};