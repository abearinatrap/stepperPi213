const { exec } = require("child_process");
const { spawn } = require("child_process");
var http = require('http').createServer(handler); //require http server, and create server with function handler()
var fs = require('fs'); //require filesystem module
var io = require('socket.io')(http) //require socket.io module and pass the http object (server)
var Gpio = require('onoff').Gpio; //include onoff to interact with the GPIO
//var LED = new Gpio(4, 'out'); //use GPIO pin 4 as output
//var pushButton = new Gpio(17, 'in', 'both'); //use GPIO pin 17 as input, and 'both' button presses, and releases should be handled

//delay between each tick of stepper turn, in milliseconds.
// positive is clockwise, negative is counterclockwise
var clickDelay=1000;

http.listen(8080); //listen to port 8080

function handler (req, res) { //create server
  fs.readFile(__dirname + '/public/index.html', function(err, data) { //read file index.html in public folder
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html'}); //display 404 on error
      return res.end("404 Not Found");
    }
    res.writeHead(200, {'Content-Type': 'text/html'}); //write HTML
    res.write(data); //write data from index.html
    return res.end();
  });
}
var stepperRun = spawn('python',['stepperSocket.py','0']);
var lightRun= spawn('python',['outletter.py','0']);
io.sockets.on('connection', function (socket) {// WebSocket Connection
  var steppervalue = 0; //static variable for current status
  var lightvalue=0;
  /**
  pushButton.watch(function (err, value) { //Watch for hardware interrupts on pushButton
    if (err) { //if an error
      console.error('There was an error', err); //output error message to console
      return;
    }
    lightvalue = value;
    socket.emit('light', lightvalue); //send button status to client
  });*/
  socket.emit('stepper',steppervalue);
  socket.emit('stepper',lightvalue);
  socket.on('stepper', function(data) { //get stepper switch status from client
    stepperRun.kill();
    steppervalue = data;
    console.log("stepper to "+steppervalue);
    //exec("python stepperSocket.py");
    stepperRun=spawn('python',['stepperSocket.py',steppervalue.toString()]);
  });
  socket.on('light', function(data) {
    lightRun.kill();
    lightvalue=data;
    console.log("light switch to "+lightvalue);
    lightRun=spawn('python',['outletter.py',lightvalue.toString()]);
    //yep
  });
});

//makes most sense to kill last process upon new data rather than wait for it to be over. especially with large delay times between ticks
//therefore start new process upon change in delay value and kill last.

process.on('SIGINT', function () { //on ctrl+c
 // LED.writeSync(0); // Turn LED off
 // LED.unexport(); // Unexport LED GPIO to free resources
  //pushButton.unexport(); // Unexport Button GPIO to free resources
  process.exit(); //exit completely
});
