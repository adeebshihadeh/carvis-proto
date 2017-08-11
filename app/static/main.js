

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

$("#toggle-fullscreen").click(function() {
  var element = document.body;

  var requestMethod = element.requestFullScreen || element.webkitRequestFullScreen || element.mozRequestFullScreen || element.msRequestFullScreen;

  if (requestMethod) { // Native full screen.
    requestMethod.call(element);
  } else if (typeof window.ActiveXObject !== "undefined") { // Older IE.
    var wscript = new ActiveXObject("WScript.Shell");
    if (wscript !== null) {
      script.SendKeys("{F11}");
    }
  }

});

window.setInterval(function() {
  var now = new Date();
  $("#display-time").text(now.toLocaleTimeString().replace(/:\d{2}\s/,' '));
}, 2000); 

function sendCommand(cmd) {
  $.post("/command", {"cmd": cmd});
}
