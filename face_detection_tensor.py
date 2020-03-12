# import necessary packages
import os, re, subprocess, time
import cvlib as cv
import cv2


# Function to test on_status
def is_on():
    on = re.search(b'mWakefulness=Awake',subprocess.check_output(['adb','shell','dumpsys','power']))
    os.system("$q")
    if on:
        return True
    else:
        return False
# Function to test unlocked_status
def is_unlocked():
    unlocked = re.search(b'mHoldingWakeLockSuspendBlocker=true',subprocess.check_output(['adb','shell','dumpsys','power']))
    os.system("$q")
    if unlocked:
        return True
    else:
        return False    
    
os.system("adb kill-server")
os.system("adb start-server")
os.system("adb kill-server")
os.system("adb start-server")
os.system("adb connect 192.168.1.5")

#Need to wait for device to connect otherwise gives error as follow: subprocess.CalledProcessError: Command '['adb', 'shell', 'dumpsys', 'power']' returned non-zero exit status 1.

time.sleep(10)
# open webcam
webcam = cv2.VideoCapture(0)

paused = ''

if not webcam.isOpened():
    print("Could not open webcam")
    exit()
    
try:
    # loop through frames
    while webcam.isOpened():

        # read frame from webcam 
        status, frame = webcam.read()

        if not status:
            print("Could not read frame")
            exit()

        # apply face detection
        faces, confidence = cv.detect_face(frame)
        
#        print(faces)
#        print(confidence)
        if faces == []:
            if paused == True:
                pass
            else:
                if is_on() and is_unlocked():
                    if paused !="":
                        os.system("adb shell input keyevent 85")
                        os.system("$q")
                    paused = True
                    print ("Pause")
        elif faces != []:
            if paused == False:
                pass
            else:
                if  is_on() and is_unlocked():
                    if paused !="":
                        os.system("adb shell input keyevent 85")
                        os.system("$q")
                    paused = False
                    print ("Play")      
        # loop through detected faces
        for idx, f in enumerate(faces):
            
            (startX, startY) = f[0], f[1]
            (endX, endY) = f[2], f[3]

            # draw rectangle over face
            cv2.rectangle(frame, (startX,startY), (endX,endY), (0,255,0), 2)

            text = "{:.2f}%".format(confidence[idx] * 100)

            Y = startY - 10 if startY - 10 > 10 else startY + 10

            # write confidence percentage on top of face rectangle
            cv2.putText(frame, text, (startX,Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                        (0,255,0), 2)

        # display output
        cv2.imshow("Real-time face detection", frame)

        # press "Q" to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break                                               
except KeyboardInterrupt:  #Stop if ctrl+c is pressed and stop capture     
    # release resources
    webcam.release()      
    os.system("adb kill-server")

