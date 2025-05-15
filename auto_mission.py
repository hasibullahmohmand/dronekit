from dronekit import connect,VehicleMode
import time
import socket
import math
import argparse
from pymavlink import mavutil
##############FUNCTIONS##########
def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument("--connect")
    args = parser.parse_args()
    connection_string = args.connect

    if not connection_string:
        import dronekit_sitl
        sitl = dronekit_sitl.start_default()
        connection_string = sitl.connection_string()

    vehicle = connect(connection_string,wait_ready=True)
    return vehicle

def arm_and_takeoff(targetHeight):
    while  vehicle.is_armable!=True:
        print("Waiting for vehicle to become armable")
        time.sleep(1)
    print("Vehicle is now armable")

    vehicle.mode = VehicleMode("GUIDED") ####switch to different vehicle modes
    while vehicle.mode !="GUIDED":
        print("Waiting for drone to enter GUIDED flight mode")
        time.sleep(1)
    print("Vehicle is now in GUIDED mode :)")

    vehicle.armed = True
    while vehicle.armed != True:
        print("Waiting for vehicle to become armed")
        time.sleep(1)
    print("Vehicle is armed now, Vehicle props are spinning now :)")
     
    vehicle.simple_takeoff(targetHeight)
    while True:
        print('Current Altitude: ' , vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt>=.95*targetHeight:
            break
        time.sleep(1)
    print("Target altitude reached!!")
    return None


#####>> python connection_template.py --connect 127.0.0.1:14550   the argparse is allowing us to add --arguments to our code like this


################MAIN EXECUTABLR##############
vehicle = connectMyCopter()


#############command Template#################
wphone = vehicle.location.global_relative_frame
cmd1=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,wphone.lat,wphone.lon,wphone.alt)
cmd2=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,44.501375,-88.062645,15)
cmd3=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,44.501746,-88.062242,10)
cmd4=Command(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_RRTURN_TO_LAUNCH,0,0,0,0,0,0,0,0,0)

##Download current list of commands from drone were connected to
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()

##clear the current commands list 
cmds.clear()

##add in our new commands
cmds.add(cmd1)
cmds.add(cmd2)
cmds.add(cmd3)
cmds.add(cmd4)

##Upload our commands ro the drone
vehicle.commands.upload()

arm_and_takeoff(10)
print("After arm and takeoff")
vehicle.mode = VehicleMode("AUTO")
while vehicle.mode!="AUTO":
    time.sleep(.2)
while vehicle.location.global_relative_frame.alt>2:
    print("Drone is executing the misssion, but we can still run code")
    time.sleep(2)
