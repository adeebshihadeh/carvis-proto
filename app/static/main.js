

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
$("button").click(function() {
  sendCommand($(this).attr('id').split("btn-")[1]);
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
