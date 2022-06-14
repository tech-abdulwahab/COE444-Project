GET:

var server = "192.168.56.1";
var serverPort = 5678;

var client;
var count = 0;

var buttonPin = 0;
var state;
var email ;
var Day ;
var Month;
var data2;
var emailArray = [];
var DayArray = [];
var i = 0;
var j = 0;
var conn;
var d;


function setup() {
	pinMode(buttonPin, INPUT);
	state = digitalRead(buttonPin);
	d = new Date();
	
	// create client
	client = new RealTCPClient();
	conn = client.connect(server, serverPort);
	if(conn){
	
	
	// when receiving data

	client.onReceive = function(data) {
		
		email = String(data);
		data2=data.split(",");
		email = data2[0];
		emailArray[i++] = email;
		Day = Number(data2[1]);
		DayArray[j++] = Day;
		count++;
	};
	
	
		EmailClient.setup(
		"omar@gmail.com",
		"gmail.com",
		"omar",
		"123"
	);
	
	EmailClient.onSend = function(status) {
		Serial.println("Sent: " + status);
	};
	
}
	
}



function loop() {
	
	var newState = digitalRead(buttonPin);
    var i;
    var s;
	if(newState != state){
		s = newState;
		client.send(s);
		Serial.println(newState);
		delay(10000);
		
		
		for(i=0; i<count ;i++){
			Serial.println(emailArray[i]);
			if(d.getUTCDate() >= DayArray[i]){
				if(d.getUTCDate() - DayArray[i] <= 14){
					EmailClient.send(emailArray[i], "Warning", "I was near to you within the past 14 days and I have been diagnosed with COVID-19 today");
				}
			}else if(d.getUTCDate() < DayArray[i]){
				if((d.getUTCDate()+30) - DayArray[i] <= 14){
					EmailClient.send(emailArray[i], "Warning", "I was near to you within the past 14 days and I have been diagnosed with COVID-19 today");
				}
				
			}else{
				continue;
			}
			Serial.println("sent to "+ i);
			
			
		}
		
	
		
		
		
	}
	
}


