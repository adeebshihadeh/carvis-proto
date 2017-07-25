

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


function sendCommand(cmd) {
  $.post("/command", {"cmd": cmd});
}
