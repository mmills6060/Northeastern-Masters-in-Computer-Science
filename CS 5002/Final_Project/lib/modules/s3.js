const fs = require('fs-extra');
const mime = require('mime-types');
const { join, basename, dirname } = require('path');
const { toSystemPath } = require('../core/path');

module.exports = {

    provider: function (options, name) {
        this.setS3Provider(name, options);
    },

    createBucket: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.createBucket: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.createBucket: bucket is required.');
        const ACL = this.parseOptional(options.acl, 'string', undefined);
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        return s3.createBucket({ Bucket, ACL });
    },

    listBuckets: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.listBuckets: provider is required.');
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        return s3.listBuckets({});
    },

    deleteBucket: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.deleteBucket: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.deleteBucket: bucket is required.');
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        return s3.deleteBucket({ Bucket });
    },

    listFiles: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.listFiles: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.listFiles: bucket is required.');
        const MaxKeys = this.parseOptional(options.maxKeys, 'number', undefined);
        const Prefix = this.parseOptional(options.prefix, 'string', undefined);
        const ContinuationToken = this.parseOptional(options.continuationToken, 'string', undefined);
        const StartAfter = this.parseOptional(options.startAfter, 'string', undefined);
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        return s3.listObjectsV2({ Bucket, MaxKeys, Prefix, ContinuationToken, StartAfter });
    },

    putFile: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.uploadFile: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.uploadFile: bucket is required.');
        const path = toSystemPath(this.parseRequired(options.path, 'string', 's3.uploadFile: path is required.'));
        const Key = this.parseRequired(options.key, 'string', 's3.uploadFile: key is required.');
        const ContentType = this.parseOptional(options.contentType, 'string', mime.lookup(Key) || 'application/octet-stream');
        const ContentDisposition = this.parseOptional(options.contentDisposition, 'string', undefined);
        const ACL = this.parseOptional(options.acl, 'string', undefined);
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        let Body = fs.createReadStream(path);

        const result = await s3.putObject({ Bucket, ACL, Key, ContentType, ContentDisposition, Body });

        try {
            const endpoint = await s3.config.endpoint();
            result.Location = `https://${Bucket}.${endpoint.hostname}/${Key}`;
        } catch (e) {}


        return result;
    },

    getFile: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.getFile: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.getFile: bucket is required.');
        const Key = this.parseRequired(options.key, 'string', 's3.getFile: key is required.');
        const path = toSystemPath(this.parseRequired(options.path, 'string', 's3.getFile: path is required.'));
        const stripKeyPath = this.parseOptional(options.stripKeyPath, 'boolean', false);
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        const file = Key;
        if (stripKeyPath) file = basename(file);
        const destination = join(path, file);

        await fs.ensureDir(dirname(destination));

        const writer = fs.createWriteStream(destination);

        const { Body } = await s3.getObject({ Bucket, Key });

        Body.pipe(writer);

        return new Promise((resolve, reject) => {
            writer.on('finish', resolve);
            writer.on('error', reject);
        });
    },

    deleteFile: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.deleteFile: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.deleteFile: bucket is required.');
        const Key = this.parseRequired(options.key, 'string', 's3.deleteFile: key is required.');
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        return s3.deleteObject({ Bucket, Key });
    },

    downloadFile: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.downloadFile: profider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.downloadFile: bucket is required.');
        const Key = this.parseRequired(options.key, 'string', 's3.downloadFile: key is required.');
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        const data = await s3.headObject({ Bucket, Key });

        this.res.set('Content-Length', data.ContentLength);
        this.res.attachment(basename(Key));

        const { Body } = await s3.getObject({ Bucket, Key });

        Body.pipe(this.res);

        this.noOutput = true;
    },

    signDownloadUrl: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.signDownloadUrl: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.signDownloadUrl: bucket is required.');
        const Key = this.parseRequired(options.key, 'string', 's3.signDownloadUrl: key is required.');
        const expiresIn = this.parseOptional(options.expires, 'number', 300);
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        const { getSignedUrl } = require("@aws-sdk/s3-request-presigner");
        const { GetObjectCommand } = require('@aws-sdk/client-s3');
        const command = new GetObjectCommand({ Bucket, Key });

        return getSignedUrl(s3, command, { expiresIn });
    },

    signUploadUrl: async function (options) {
        const provider = this.parseRequired(options.provider, 'string', 's3.signUploadUrl: provider is required.');
        const Bucket = this.parseRequired(options.bucket, 'string', 's3.signUploadUrl: bucket is required.');
        const Key = this.parseRequired(options.key, 'string', 's3.signUploadUrl: key is required.');
        const ContentType = this.parseOptional(options.contentType, 'string', mime.lookup(Key) || 'application/octet-stream');
        const expiresIn = this.parseOptional(options.expires, 'number', 300);
        const ACL = this.parseOptional(options.acl, 'string', undefined);
        const s3 = this.getS3Provider(provider);

        if (!s3) throw new Error(`S3 provider "${provider}" doesn't exist.`);

        const { getSignedUrl } = require("@aws-sdk/s3-request-presigner");
        const { PutObjectCommand } = require('@aws-sdk/client-s3');
        const command = new PutObjectCommand({ Bucket, Key, ContentType, ACL });

        return getSignedUrl(s3, command, { expiresIn });
    }

};