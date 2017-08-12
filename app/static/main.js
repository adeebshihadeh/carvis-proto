var socket = io.connect("http://localhost:8080");

socket.on('connect', function() {
  console.log("socket connected");

  $("#server-status").text("server connected");
});

socket.on('disconnect', function() {
  console.log("socket disconnected");

  $("#server-status").text("server disconnected");
});

function sendCommand(cmd) {
  $.post("/command", {"cmd": cmd});
}

function updateTime() {
  var now = new Date();
  $("#display-time").text(now.toLocaleTimeString().replace(/:\d{2}\s/,' '));
}

// auto bind all buttons
$("[id^=btn").click(function() {
  sendCommand($(this).attr('id').split("btn-")[1]);
});


// handle audio stuff 
$("[id^=audio").click(function() {
  var id = $(this).attr('id');
  if(id == "audio-playpause" ) {
    socket.emit("audio", "playpause");
  } else if (id == "audio-previous") {
    socket.emit("audio", "previous");
  } else if (id == "audio-next") {
    socket.emit("audio", "next");
  } else {
    console.log("unimplemented audio function: " + id);
  }
});

window.setInterval(function() {
  updateTime()
}, 2000);

$(document).ready(function() {
  updateTime();
});
