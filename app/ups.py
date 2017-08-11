import sys
from threading import  Thread
import raspiupshat
import time

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
    else:
      print "charge level: " + str(getCharge())
    time.sleep(1)

def init():
  try:
    thread_ = Thread(target = check)
    thread_.start()
    print "started ups thread"
  except Exception as e:
    print "failed to create ups thread"
    raise