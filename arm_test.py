from dronekit import connect, VehicleMode, LocationGlobalRelative, APIException
import time
import socket
import exceptions
import math
import argparse

def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect')
    args = parser.parse_args()

    connection_string = args.connect
    baud_rate = 57000

    vehicle = connect(connection_string,baud=baud_rate,wait_ready=True)
    return vehicle

def arm():
    while vehicle.is_armable==False:
        print("Waiting for vehicle to become armable..")
        time.sleep(1)
    print("Your vehicle is now armable")

    vehicle.armed=True
    while vehicle.armed=False:
        print("Waiting for drone to become armed..")
        time.sleep(1)

    print("Vehicle is now armed..")
    
    return None

vehicle = connectMyCopter()
arm()
print("End of the script")