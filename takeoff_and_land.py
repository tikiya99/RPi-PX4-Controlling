from dronekit import connect, VehicleMode, LocationGlobalRelative
import time
import argparse

def connectMyCopter():
    parser = argparse.ArgumentParser(description='commands')
    parser.add_argument('--connect', help="Vehicle connection target string.")
    args = parser.parse_args()

    connection_string = args.connect

    vehicle = connect(connection_string, wait_ready=True)
    return vehicle

def arm_and_takeoff(vehicle, aTargetAltitude):
    while not vehicle.is_armable:
        print("Waiting for vehicle to become armable")
        time.sleep(1)

    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    while vehicle.mode != "GUIDED":
        print("Waiting for vehicle to enter GUIDED mode")
        time.sleep(1)

    vehicle.armed = True
    while not vehicle.armed:
        print("Waiting for vehicle to become armed")
        time.sleep(1)

    print("Taking off!")
    vehicle.simple_takeoff(aTargetAltitude)

    while True:
        print("Current Altitude: %d" % vehicle.location.global_relative_frame.alt)
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

vehicle = connectMyCopter()
print("About to take off...")

target_altitude = 10  #Desired Takeoff Altitude
arm_and_takeoff(vehicle, target_altitude)

print("Landing...")
vehicle.mode = VehicleMode("LAND")

while vehicle.armed:
    time.sleep(1)

print("End of function")
print("Arducopter version: %s" % vehicle.version)

vehicle.close()
