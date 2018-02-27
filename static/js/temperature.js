var wsaddr = window.location.host;
var ws_scheme = window.location.protocol === "https:" ? "wss" : "ws";
var path = window.location.pathname.replace(/\/$/, "");
var wsUri = ws_scheme + "://" + wsaddr + path + "/ws/";
var websocket;

function setupWebSocket() {
	websocket = new WebSocket(wsUri);
	websocket.open = function(evt) { onOpen(evt) };
	websocket.onMessage = function(evt) { onMessage(evt) };
}

function opOpen(evt) {
	console.log("connected to websocket");
}

function onMessage(evt) {
	var data = JSON.parse(evt.data);
	console.log("received message");
	console.log(evt);
	$('#mTemp').text(evt.data);
}

window.addEventListener("load", setupWebSocket, false);
