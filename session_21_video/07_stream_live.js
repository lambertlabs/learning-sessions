const NodeMediaServer = require('node-media-server');

const config = {
  rtmp: {
    port: 1935,
    chunk_size: 60000,
    gop_cache: false,
    ping: 30,
    ping_timeout: 60
  },
  http: {
    port: 8000,
    mediaroot: './media',
    allow_origin: '*'
  },
  trans: {
    ffmpeg: '/usr/bin/ffmpeg',
    tasks: [
        {
            app: 'live',
            ac: 'acc',
            vc: 'copy',
            hls: true,
            hlsFlags: '[hls_time=2:hls_list_size=3:hls_flags=delete_segments]',
        }
    ]
  }
};

var nms = new NodeMediaServer(config)
nms.run();
