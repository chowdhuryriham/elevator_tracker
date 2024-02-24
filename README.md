## Smart Elevator Project

This project aims to create a smart elevator system using Raspberry Pi, Python, OpenCV, and Firebase.

### Purpose
Efficiently tracks elevator positions in high-rise buildings, providing real-time updates to reduce wait times and enhance user experience. This device will be positioned above the elevator display, allowing it to read the digits shown. It's designed to be portable and will display the same digit on its display as well as send it to the user.

### Features
- Real-time position tracking
- Live updates accessible via web app
- Optimizes traffic flow and minimizes congestion
- Enhances safety and accessibility

### Benefits
- Improved user experience
- Increased building efficiency
- Enhanced safety measures
- Reduced environmental impact: minimizing unnecessary stops

### Future Enhancements
- Predictive analytics for demand forecasting
- Integration with smart building systems

### Conclusion
The Elevator Tracker streamlines building navigation, offering real-time updates to optimize efficiency and enhance user convenience in high-rise environments.

### Project Components

#### 1. `smart_elevator.py`
   - This Python script captures images from a PiCamera, processes them using OpenCV, and detects floors using image subtraction techniques.
   - It utilizes `picamera`, `opencv-python`, and `imutils` libraries.

#### 2. `smartElevatorReference.py`
   - This script captures images from a PiCamera, processes them using OpenCV, and saves them for reference images for floor detection.
   - It also uses `picamera`, `opencv-python`, and `imutils` libraries.

#### 3. `ReferenceCreation.py`
   - This script processes reference images for floor detection.
   - It utilizes `opencv-python` and `imutils` libraries.

#### 4. `lscDriver.py`
   - This Python script provides driver functionality for an LCD connected via I2C.
   - It communicates with the LCD screen to display messages.
   - It relies on `i2c_lib.py`.

#### 5. `lcd.py`
   - This script demonstrates how to use the `lscDriver.py` to display messages on an LCD screen.
   - It depends on `lcddriver` library.

#### 6. `i2c_lib.py`
   - This Python module provides low-level I2C communication functions.
   - It is utilized by `lscDriver.py` for communicating with the LCD.

#### 7. `firebase.py`
   - This script demonstrates how to interact with Firebase Realtime Database.
   - It uses the `firebase` library.

### How to Use
1. Connect the Raspberry Pi camera module.
2. Ensure all required libraries are installed (`picamera`, `opencv-python`, `imutils`, `firebase`).
3. Run `smart_elevator.py` to start the smart elevator system.
4. The system will capture images, process them, and detect floors. Detected floor information will be sent to Firebase Realtime Database.
5. You can use the `firebase.py` script to update floor information manually.

### Note
- Make sure to configure Firebase with your own Firebase Realtime Database URL.
- Adjust camera settings and floor detection algorithms as needed for your specific environment.

### References
- [picamera Documentation](https://picamera.readthedocs.io/en/release-1.13/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Firebase Documentation](https://firebase.google.com/docs/database)
