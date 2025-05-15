from dronekit import connect
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

#####>> python connection_template.py --connect 127.0.0.1:14550   the argparse is allowing us to add --arguments to our code like this


################MAIN EXECUTABLR##############
vehicle = connectMyCopter()

gps_type = vehicle.parameters['GPS_TYPE']
print("GPS_type param value is:" +str( gps_type))
vehicle.parameters['GET_TYPE'] = 3
gps_type = vehicle.parameters['GPS_TYPE']
print("GPS_type param value is:" + str(gps_type))
if gps_type != 4:
    vehicle.parameters['GET_TYPE'] = 4
    gps_type = vehicle.parameters['GPS_TYPE']
print("GPS_type param value is:" + str(gps_type))

