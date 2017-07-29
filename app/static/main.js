

/*
  TODO
    - auto retrieve http port
    - detect server status
    - better touch interaction (hover, active, etc.)
*/

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
  console.log("interval");
  var now = new Date();
  $("#display-time").text(now.toLocaleTimeString().replace(/:\d{2}\s/,' '));
}, 2000); 

function sendCommand(cmd) {
  $.post("/command", {"cmd": cmd});
}
