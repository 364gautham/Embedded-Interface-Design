// Gautham Kashim : Code referred from https://github.com/momenso/node-dht-sensor/blob/master/README.md
// Node Version : v8.12.0

var sensorLib = require("node-dht-sensor");
var i=0;var lowt,hight,avgt,lowh,highh,avgh;
var sensor = {
    sensors: [{
        name: "Outdoor",
        type: 22,
        pin: 4
    } ],
    read: function() {
	i++;
	if(i>10)i=1;
        for (var a in this.sensors) {
            var b = sensorLib.read(this.sensors[a].type, this.sensors[a].pin);
	    var c=b.temperature.toFixed(1);
	    c=(c*9/5) + 32; 
	    var d=b.humidity.toFixed(1);d=d*1;
            console.log(i+"- "+"Temp " + ": " +
              c.toFixed(2) + "degF, " + "Hum : " +d.toFixed(2) + "%");
        }
	if(i==1){lowt = c;hight=c;lowh=d;highh=d;avgt=c;avgh=d;}
	if(i>1){
		avgt = (avgt*(i-1)+c)/i;
		avgh = (avgh*(i-1)+d)/i;
	}
	if(lowt>c)lowt=c;
	if(hight<c)hight=c;
	if(lowh>d)lowh=d;
	if(highh<d)highh=d;
	if(i==10){
		console.log("lowest Temp : "+lowt +"\n"+ "highest Temp:" + hight+
			"\n"+"lowest hum : "+lowh +"\n"+ "highest hum:" + highh+
			"\n"+"avg temp :" + avgt.toFixed(2)+"\n"+"avg Hum :" + avgh.toFixed(2));
	}
        setTimeout(function() {
            sensor.read();
        }, 1000);
    }
};

sensor.read();