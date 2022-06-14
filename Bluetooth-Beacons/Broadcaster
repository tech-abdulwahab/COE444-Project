var DEFAULT_BEACON_UUID = "{00000000-0000-0000-0000-111111111111}";
var DEFAULT_BEACON_DATA = "omar@gmail.com";

function setup() {
	Bluetooth.init();
	Bluetooth.enableBroadcast(true);
	
	var uuid = getDeviceProperty(getName(), "beaconUuid");
	if (uuid == null)
		setDeviceProperty(getName(), "beaconUuid", DEFAULT_BEACON_UUID);

	var data = getDeviceProperty(getName(), "beaconData");
	if (data == null)
		setDeviceProperty(getName(), "beaconData", DEFAULT_BEACON_DATA);
}

function loop() {
	var uuid = getDeviceProperty(getName(), "beaconUuid");
	var data = getDeviceProperty(getName(), "beaconData");

	Serial.println("Broadcasting to " + uuid);
	Bluetooth.broadcastBeacon(uuid, data);
	
	delay(10000);
}
