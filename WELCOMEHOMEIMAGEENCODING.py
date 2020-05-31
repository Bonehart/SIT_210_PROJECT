from imutils import paths
import face_recognition
import argparse
import pickle
import cv2
import os

path = 'photos'
knownEncodings = []
knownNames = []
imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

for imagePath in imagePaths:
    print(imagePath)
    name = imagePath.split(".")[1]
    print(name)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb,
        model='hog')
    encodings = face_recognition.face_encodings(rgb, boxes)
    
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
        
data = {"encodings": knownEncodings, "names": knownNames}
f = open('pickle', "wb")
f.write(pickle.dumps(data))
f.close()