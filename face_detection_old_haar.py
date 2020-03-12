import os, re, subprocess, time
import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Function to test on_status
def is_on():
    on = re.search(b'mWakefulness=Awake',subprocess.check_output(['adb','shell','dumpsys','power']))
    os.system("$q")
    if on:
        return True
    else:
        return False

# To capture video from webcam. 

os.system("adb kill-server")
os.system("adb start-server")
os.system("adb kill-server")
os.system("adb start-server")
os.system("adb connect 192.168.1.5") #Connects to firetv with ip address 192.168.1.3
time.sleep(30)

cap = cv2.VideoCapture(0)
paused = ''
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

#Function to test if unlocked
def is_unlocked():
"""Checks if the fire tv is unlocked"""
# The search string in re.search needs to be a byte-like object not string so prefix string with b, EX: b'test string'  
    unlocked = re.search(b'mHoldingWakeLockSuspendBlocker=true',subprocess.check_output(['adb','shell','dumpsys','power']))
    os.system("$q")
    if unlocked:
        return True
    else:
        return False    
try:
    while True:
        # Read the frame
        _, img = cap.read()
        # Convert to grayscale
        # Detect the faces
        faces = face_cascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1, 4)
        # Draw the rectangle around each face
        if faces == ():
            if paused == True:
                pass
            else:
                if is_on() and is_unlocked():
                    if paused !="":
                        os.system("adb shell input keyevent 85")
                        os.system("$q")
                    paused = True
                    print ("Pause")
        elif faces != ():
            if paused == False:
                pass
            else:
                if  is_on() and is_unlocked():
                    if paused !="":
                        os.system("adb shell input keyevent 85")
                        os.system("$q")
                    paused = False
                    print ("Play")                    
#    # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # Display
        cv2.imshow('img', img)
        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
except KeyboardInterrupt:  #Stop if ctrl+c is pressed and stop capture          
    # Release the VideoCapture object 
    cap.release()
    os.system("adb kill-server")
