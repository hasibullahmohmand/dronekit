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

def condition_yaw(degree,ralative):
    if relative:
         is_relative =1 #yaw is relative to direction of travel
    else:
         is_ralative = 0 #yaw is the absolute angle
    msg = vehicle.message_factory.command_long_encode(
            0, 0,               #target system, target component
            mavutil.mavlink.MAV_CMD_CONDITION_YAW,#command
            0, #conformation
            degree,             #param1, yaaw in degrees
            0,            #param2, yaw speed deg/s
            1,           #param3, direction -1 ccw, 1cw
            is_relative,            #param4, relative offset 1, absolute angle 0
            0, 0, 0)               #param5 -7 not used
    vehicle.send_mavlink(msg)
    vehicle.flush()
def dummy_yaw_initializer():
    lat = vehicle.location.global_relative_frame.lat
    lon= vehicle.location.global_relative_frame.lon
    alt = vehicle.location.global_relative_frame.alt
    aLocation = LocationGlobalRelative(lat,lon,alt)

    msg = vehicle.message_factory.command_long_encode(
            0,                  #time_boot_ms (not used)
            0, 0,               #target system, target component
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,#frame
            0b0000111111000111, #--BITMASK -> Consider only the velocities
            aLocation.lat*1e7,            #--lat
            aLocation.lon*1e7,           #--lon
            aLocation.alt*1e7,            #--alt
            0, #x velocity
            0, #y velocity
            0, #z velocity
            0, 0, 0, #afx, afy, afz accelerations
            0, 0,)               #--YAW, YAW_RATE
    vehicle.send_mavlink(msg)
    vehicle.flush()


#####>> python connection_template.py --connect 127.0.0.1:14550   the argparse is allowing us to add --arguments to our code like this


################MAIN EXECUTABLR##############
vehicle = connectMyCopter()
arm_and_takeoff(10)
dummy_yaw_initializer()
time.sleep(2)

condition_yaw(30,1)
print("Yawing 30 degrees relative to current position")
time.sleep(7)

print("Yawing TRUE NORTH")
condition_yaw(0,0)
time.sleep(7)
print("Yawing TRUE WEST")
condition_yaw(270,0)
while True:
    time.sleep(1)
