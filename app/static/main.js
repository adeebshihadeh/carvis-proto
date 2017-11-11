var socket = io.connect("http://localhost:8080");

socket.on('connect', function() {
  console.log("socket connected");

  $("#server-status").text("connected");
});

socket.on('disconnect', function() {
  console.log("socket disconnected");

  $("#server-status").text("disconnected");
});

socket.on('msg', function(msg) {
  console.log("new sock msg");
  msg = JSON.parse(msg);

  console.log(msg);
  
  if (msg.Audio) {
    if (msg.Audio.song.title) {
      $("#audio-primary-info").text(msg.Audio.song.title);
      $("#audio-secondary-info").text(msg.Audio.song.artist);
      $("#audio-album-art").show().attr("src", msg.Audio.song.artUrl);
    } else {
      $("#audio-primary-info").text("song");
      $("#audio-secondary-info").text("not playing");
      $("#audio-album-art").hide();
    }

    $("#audio-playpause").html('<i class="fa fa-' + (msg.Audio.paused ? 'play' : 'pause') + '"></i>');
  } else {
    alert("msg not audio")
  }
});

function updateTime() {
  var now = new Date();
  $("#display-time").text(now.toLocaleTimeString().replace(/:\d{2}\s/,' '));
}

function sendCommand(module, cmd) {
  socket.emit("cmd", JSON.stringify({module: cmd}));
}

// handle audio stuff 
$("[id^=audio").click(function() {
  var id = $(this).attr('id');
  if(id == "audio-playpause" ) {
    sendCommand("audio", $("#audio-playpause").html().includes("pause") ? "pause" : "play");
  } else if (id == "audio-previous") {
    sendCommand("audio", "previous");
  } else if (id == "audio-next") {
    sendCommand("audio", "next");
  } else {
    console.log("unimplemented audio function: " + id);
  }
});

$("#volume-toggle").click(function() {
  $("#volume-toggle-off").toggle();
  $("#volume-toggle-on").toggle();
  socket.emit("system", "mute-" + ($("#volume-toggle-on").is(":visible") ? "off" : "on"));
});

$("*").bind("touchstart", function() {
  $(this).css("cursor", "none");
});

window.setInterval(function() {
  updateTime()
}, 2000);

$(document).ready(function() {
  updateTime();
  $("#volume-toggle-off").hide();

  // for debugging
  if (screen.height > screen.width) {
    $("body").css("position", "fixed");
    $("body").css("overflow", "hidden");
  }
});


function map() {
  var mapProp= {
    center:new google.maps.LatLng(37.7749, -122.4194),
    zoom: 12,
  };
  var map=new google.maps.Map(document.getElementById("map"),mapProp);
}