
MrMagoo Magoo <nickcrowle@gmail.com>
11:57 PM (1 minute ago)
to me

from imutils import paths
from imutils.video import VideoStream
from imutils.video import FPS
import face_recognition

import pickle
import cv2
import os

import imutils
import time
import paho.mqtt.client as mqtt

users_file = open('users.pkl', 'rb')
dic = pickle.load(users_file)
users_file.close()

ourClient = mqtt.Client("TEST")
ourClient.connect("test.mosquitto.org", 1883)
ourClient.loop_start()


def runRoutines(name):
    for i in dic[name]:
        print(i)
        ourClient.publish("WELCOME_HOME", i)  
        time.sleep(1)

vs = VideoStream().start()

print("[INFO] loading encodings + face detector...")
data = pickle.loads(open('pickle', "rb").read())
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# loop over frames from the video file streamxz
while True:
   
    #this code is standard code for reading the faces of people and storing the location in a box
    #encodings require to know the location of the face to encode the actual face data
    frame = vs.read()
    frame = imutils.resize(frame, width=500)
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
   
    faceArea = detector.detectMultiScale(gray, scaleFactor=1.1,
        minNeighbors=5, minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE)
   
    boxes = [(y, x + w, y + h, x) for (x, y, w, h) in faceArea]

    #thewse are encodings read by the camera we compare them to those saved in the pickle file
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []
    Matched = False
   
    for encoding in encodings:
 
        matches = face_recognition.compare_faces(data["encodings"],encoding)
        name = "UNdefined"
       
        if(Matched== True):
            print("Your settings have been applied, welcome home", name)
            break
       
        #loop over all mathes and take action for the first one found if one is found the program breaks
        #this is because we don't want repeated things turning on and off
        if True in matches:
           
            #matchedfaces = [i for (i, b) in enumerate(matches) if b]
            #counts = {}
            Matched = True

            #for i in matchedfaces:
            name = data["names"][0]
       
                                 
            print("welcome home ",name)
            print("actioning your welcome home settings")
            time.sleep(1)
            runRoutines(name)
                       
            break;

    # standard code to display the image to our screen
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
   
    # if a matche was found tyhe program needs to end
    if(Matched==True):
        print("Your settings have been applied, welcome home", name)
        break

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break


# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()



