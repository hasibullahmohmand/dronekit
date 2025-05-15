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
### Send a velocity command with  +x being the heading of the drone
def send_local_ned_velocity(vx,vy,vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,                  #time_boot_ms (not used)
            0, 0,               #target system, target component
            mavutil.mavlink.MAV_FRAME_BODY_OFFSET_NED,#frame
            0b0000111111000111, #--BITMASK -> Consider only the velocities
            0, 0, 0,            #--POSITION 
            vx,vy,vz,           #--VELOCITY
            0, 0, 0,            #--ACCELERATION
            0, 0)               #--YAW, YAW_RATE
    vehicle.send_mavlink(msg)
    vehicle.flush()
### Send a velocity command with  +x being true North of Earth 
def send_global_ned_velocity(vx,vy,vz):
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
            0,                  #time_boot_ms (not used)
            0, 0,               #target system, target component
            mavutil.mavlink.MAV_FRAME_LOCAL_NED,#frame
            0b0000111111000111, #--BITMASK -> Consider only the velocities
            0, 0, 0,            #--POSITION 
            vx,vy,vz,           #--VELOCITY
            0, 0, 0,            #--ACCELERATION
            0, 0)               #--YAW, YAW_RATE
    vehicle.send_mavlink(msg)
    vehicle.flush()


#####>> python connection_template.py --connect 127.0.0.1:14550   the argparse is allowing us to add --arguments to our code like this


################MAIN EXECUTABLR##############
vehicle = connectMyCopter()
arm_and_takeoff(10)


counter = 0
while counter<5:
    send_local_ned_velocity(5,0,0)
    time.sleep(1)
    print("Moving NORTH relative to front of drone")
    counter = counter + 1

time.sleep(2)

counter = 0
while counter <5:
    send_local_ned_velocity(0,-5,0)
    time.sleep(1)
    print("Moving WEST relative to front of drone")
    counter = counter + 1

counter = 0
while counter<5:
    send_global_ned_velocity(5,0,0)
    time.sleep(1)
    print("Moving TRUE NORTH relative to front of drone")
    counter = counter + 1

time.sleep(2)

counter = 0
while counter <5:
    send_global_ned_velocity(0,-5,0)
    time.sleep(1)
    print("Moving TRUE WEST relative to front of drone")
    counter = counter + 1
####UP AND DOWN
counter = 0
while counter<5:
    send_local_ned_velocity(0,0,5)
    time.sleep(1)
    print("Moving UP relative to front of drone")
    counter = counter + 1

time.sleep(2)

counter = 0
while counter <5:
    send_global_ned_velocity(0,0,-5)
    time.sleep(1)
    print("Moving down relative to front of drone")
    counter = counter + 1


while True:
    time.sleep(1)
