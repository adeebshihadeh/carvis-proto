

/*
  TODO
    - auto retrieve http port
    - detect server status
    - better touch interaction (hover, active, etc.)
*/


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
    console.log("audio: playpause");
    
  } else if (id == "audio-previous") {
    console.log("audio: previous");
  } else if (id == "audio-next") {
    console.log("audio: next");
  } else {
    console.log("unimplemented audio function: " + id);
  }
});

$("#btn-update").click(function() {
  bootbox.confirm("update?", function(e) {
    if (e) {
      $.post("/update");
      location.reload(true);
    }
  });
});

window.setInterval(function() {
  updateTime()
}, 2000);

$(document).ready(function() {
  updateTime();
});
