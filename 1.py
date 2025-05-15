from dronekit import connect, VehicleMode

# Connect to the Vehicle (replace connection_string with your vehicle's address)
connection_string = '127.0.0.1:14550'  # Example for a simulated vehicle
print(f"Connecting to vehicle on: {connection_string}")
vehicle = connect(connection_string, wait_ready=True)

# Print some vehicle attributes
print(f"Vehicle GPS: {vehicle.gps_0}")
print(f"Vehicle Battery: {vehicle.battery}")
print(f"Vehicle Mode: {vehicle.mode.name}")

# Close the vehicle object before exiting the script
vehicle.close()

