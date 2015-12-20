"use strict";

var
  fs = require('fs'),
  net = require('net'),
  filename = process.argv[2],

  server = net.createServer(function(connection){
    // reporting
    console.log('Subscriber connected.');
    connection.write(JSON.stringify({
      type: "watching",
      file: filename}) + "\n");
    // watcher setup
    var watcher = fs.watch(filename, function(){
      connection.write(JSON.stringify({
        type: "change",
        file: filename,
        timestamp: Date.now()}) + "\n");
    });
    // clean up
    connection.on('close', function(){
      console.log('Subscriber disconnected.');
      watcher.close();
    });

  });

if (!filename) {
  throw Error('No target file was specified.');
}

server.listen(5090, function(){
  console.log('Listening for subscribers...');
});
