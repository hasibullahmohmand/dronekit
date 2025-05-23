from dronekit import connect,VehicleMode,LocationGlobalRelative
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

def get_distance_meters(targetLocation,currentLocation):
    dLat = targetLocation.lat - currentLocation.lat
    dLon = targetLocation.lon - currentLocation.lon
    return math.sqrt((dLon*dLon)+(dLat*dLat))*1.113195e5

def goto(targetLocation):
    distanceToTargetLocation = get_distance_meters(targetLocation,vehicle.location.global_relative_frame)
    
    vehicle.simple_goto(targetLocation)

    while vehicle.mode.name=="GUIDED":
        currentDistance = get_distance_meters(targetLocation,vehicle.location.global_relative_frame)
        if currentDistance<distanceToTargetLocation*.01:
            print("Reached the target waypoint")
            time.sleep(2)
            break
        return None


#####>> python connection_template.py --connect 127.0.0.1:14550   the argparse is allowing us to add --arguments to our code like this


################MAIN EXECUTABLR##############
wp1 = LocationGlobalRelative(44.50202,-88.060316,10)

vehicle = connectMyCopter()
arm_and_takeoff(10)
goto(wp1)
vehicle.mode = VehicleMode("LAND")
while vehicle.mode != "LAND":
    print("Waitting for drone to enter LAND Mode")
    time.sleep(1)
print("Vehicle in LAND Mode :)")
while True:
    time.sleep(1)

