from dronekit import connect,VehicleMode
import time
import socket
import math
import argparse
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
arm_and_takeoff(10)
