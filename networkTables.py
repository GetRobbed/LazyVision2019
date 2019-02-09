# run with python networkTables.py 10.2.19.2
#!/usr/bin/env python3
#
# This is a NetworkTables client (eg, the DriverStation/coprocessor side).
# You need to tell it the IP address of the NetworkTables server (the
# robot or simulator).
#
# When running, this will continue incrementing the value 'dsTime', and the
# value should be visible to other networktables clients and the robot.
#

import os
import sys
import time
import threading
from networktables import NetworkTables

# To see messages from networktables, you must setup logging
import logging

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)
ip= '10.2.19.2'
#ip = sys.argv[1]

NetworkTables.initialize(server=ip)

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server=ip)
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

# Insert your processing code here
print("Connected!")


sd = NetworkTables.getTable("SmartDashboard")


i = 0
while True:
    os.system("/home/pi/robo219.py")
    #m= os.system("/home/pi/LazyVision.py")
    sd.putNumber("slope", os.system("/home/pi/LazyVision.py 1"))
    #sd.putNumber("testinggucci", 2192192219)
    #sd.putNumber("b", b)
    print("robotTime:", sd.getNumber("robotTime", "N/A"))

    sd.putNumber("dsTime", i)
    time.sleep(1)
    i += 1

#table = NetworkTables.getTable('SmartDashboard')

# This retrieves a boolean at /SmartDashboard/foo
#foo = table.getBoolean('foo', True)

#subtable = table.getSubTable('bar')

# This retrieves /SmartDashboard/bar/baz
#baz = table.getNumber('baz', 1)
