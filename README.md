# Firestick face control
This python project makes use of facial recognition algorithm to detect if a person is not watching media playing on the firestick and sends commands to the firestick over adb to pause the media. 
<br/>
<br/>
If a persons face is detected again then the program sends a command to the firestick to start playing the media again. The project was tested successfully using laptop webcam and also tested using a camera module connected to a raspberry pi. There are a number of adb commands that can be used to control the firestick that could be used to improve the projects capabilities.

## Setup

1. Raspberry Pi Zero W or other wifi enabled Rpi models running Raspbian.
2. Raspberry Pi compatible camera.
3. Connect the camera to raspberry pi and power up the Pi.
4. Install the following dependencies in Raspbian:
   - tensorflow==1.13.1
   - opencv-python==3.4.6.27
   - android-tools-adb 
   - android-tools-fastboot
5. Make sure both the fireTV stick and the raspberry pi are on the same wiFi network. 
6. Connect fireTV stick to the raspberry pi via ADB.
7. Start playing any media and the raspberry Pi will automatically pause when you look away and resume playing when you look at the screen again.
