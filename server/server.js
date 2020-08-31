
var http = require('http');
var fs = require('fs');


function send404Message(response) {
    response.writeHead(404, { "Content-Type": "text/plain" });
    response.write("404 ERROR... ");
    response.end();
}

function onRequest(request, response) {
    if (request.method == 'GET' && request.url == '/index') {
        response.writeHead(200, { "Content-Type": "text/html" }); 
        fs.createReadStream("../UI/main/index.html").pipe(response); 
    }
    else if(request.method == 'GET' && request.url == '/calendar') {
        response.writeHead(200, { "Content-Type": "text/html" }); 
        fs.createReadStream("../UI/calendar/src/calendar.html").pipe(response); 

    }
    else {
        send404Message(response);
    }
}

http.createServer(onRequest).listen(8000);
console.log("Server Created...");
