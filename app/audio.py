

state = ""


def handle_request(req):
  if "playpause" in req:
    playpause()
  elif "next" in req:
    next_track()
  elif "previous" in req:
    previous_track()

def playpause():
  print "playpausing"
  return ""

def next_track():
  print "nexttracking"
  return ""

def previous_track():
  print "previoustracking"
  return ""