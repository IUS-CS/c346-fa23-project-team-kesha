

const db = client.db(dbName);

const bucket = new mongodb.GridFSBucket(db, { bucketName: 'playlist' });

fs.createReadStream('/Users/noahtrejo/MP3-FIles/Earth.mp3').
     pipe(bucket.openUploadStream('/Users/noahtrejo/MP3-FIles/Earth.mp3', {
         chunkSizeBytes: 1048576,
         metadata: { field: 'myField', value: 'myValue' }
     }));

bucket.openDownloadStreamByName('Earth.mp3').
     pipe(fs.createWriteStream('/Users/noahtrejo/Playlist/Earth.mp3'));