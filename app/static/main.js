

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

function sendCommand(cmd) {
  $.post("/command", {"cmd": cmd});
}
