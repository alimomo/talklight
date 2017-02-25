



/*

get the text submitted by client 'message'
get the form & output IDs of the HTML code

*/

var myWindow; //if window has been closed

var inputBox = document.getElementById("message");
var output = document.getElementById("output");
var form = document.getElementById("form");

try {

    // a variable with an address
    //var host = "ws://" + window.location.hostname + ":9876/websocket";
    var host = "ws://192.168.1.3:9876"
    console.log("Host:", host);

    /* create a new websocket & pass in websocket address */
    var s = new WebSocket(host, 'chat');

    //open websocket
    s.onopen = function (e) {
        console.log("Socket opened.");
    };

    //close websocket
    s.onclose = function (e) {
        console.log("Socket closed.");
    };

    //everytime you send via websocket, you append the
    s.onmessage = function (e) {
        console.log("Socket message:", e.data);
        var p = document.createElement("p");
        p.innerHTML = e.data;
        output.appendChild(p);
    };

    //websocket on error
    s.onerror = function (e) {
        console.log("Socket error:", e);
    };

} catch (ex) {
    console.log("Socket exception:", ex);
}

//on submit send input messages to the server
form.addEventListener("submit", function (e) {
    e.preventDefault();
    s.send(inputBox.value);
    inputBox.value = "";
}, false)

//send 'exit' command back to the server to exit from the client
document.getElementById("exit").addEventListener("click", function() {
    s.send('exit77');
});

if (myWindow.closed){
    s.send('exit77');
}

