# DroneKit Examples by Hasibullah Mohmand

This repository offers a collection of Python scripts utilizing the DroneKit-Python library to demonstrate various drone operations, including connection setup, mission automation, movement control, and parameter management.

## Repository Structure

* `dronekit-env/`: Environment setup files for DroneKit.
* `1.py`: Initial test script for basic DroneKit functionality.
* `auto_mission.py`: Automates a complete mission with takeoff, waypoint navigation, and landing.
* `basic_template.py`: A template showcasing the fundamental structure of a DroneKit script.
* `connection_template.py`: Demonstrates how to establish a connection with a drone.
* `location_based_movement.py`: Commands the drone to move to specific GPS coordinates.
* `mode_setter.py`: Script to change the drone's flight mode.
* `parameter_setter_and_getter.py`: Shows how to read and write drone parameters.
* `velocity_based_movement.py`: Controls the drone's movement using velocity vectors.
* `yaw_control.py`: Adjusts the drone's yaw orientation.

## Getting Started

### Prerequisites

* Python 3.6 or higher
* [DroneKit-Python](https://github.com/dronekit/dronekit-python)
* [MAVProxy](https://github.com/ardupilot/MAVProxy) (optional, for advanced simulations)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/hasibullahmohmand/dronekit.git
   cd dronekit
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install dronekit
   ```

   *Note: If using SITL (Software In The Loop) simulation, install `dronekit-sitl`:*

   ```bash
   pip install dronekit-sitl
   ```

## Running the Examples

1. **Start SITL (if not connected to a real drone):**

   ```bash
   dronekit-sitl copter
   ```

   This will start a simulated drone on `127.0.0.1:14550`.

2. **Run a Script:**

   ```bash
   python auto_mission.py
   ```

   *Ensure the script's connection string matches the SITL or real drone's address.*

## Resources

* [DroneKit-Python Documentation](https://dronekit-python.readthedocs.io/en/latest/)
* [DroneKit Forums](http://discuss.dronekit.io/)
* [ArduPilot SITL Simulator](https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html)

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open-source and available under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

---

*Disclaimer: This repository is a personal collection of DroneKit examples and is not affiliated with the official DroneKit project.*
