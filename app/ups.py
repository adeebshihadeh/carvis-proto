import sys
import thread
import raspiupshat

raspiupshat.init()

threshold_charge = 95 

def getCharge():
  return raspiupshat.getsoc()

def getVoltage():
  return raspiupshat.getv()

def check():
  while 1:
    if getCharge() < threshold_charge:
      print "system shutting down. battery below %d" % threshold_charge
      os.system("sudo shutdown")

def init():
  try:
    thread.start_new_thread(check)
  except Exception as e:
    print "failed to create thread"
    raise