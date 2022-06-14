POST

var beaconUuid = "{00000000-0000-0000-0000-222222222222}";
var service;
var server = "192.168.56.1";
var serverPort = 1234;
var client;
var count = 0;
var d;

function setup() {
	// create client
	client = new RealTCPClient();
	// connect to server
	client.connect(server, serverPort);
	service = new BluetoothService();
	// start service
	Serial.println(service.start(beaconUuid));
	
	d = new Date();
	

}



function loop() {

	service.onReceive = function(srcMac, srcService, dstMac, dstService, data) {
	Serial.println("received beacon from "
		+ "Ali" + ": " + data);
		client.send(data + "," +d.getUTCDate());
	
	};
	

}
