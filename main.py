import cv2
import tkinter.filedialog as file
from pymongo import MongoClient
import face_recognition
import numpy as np


client = MongoClient("mongodb+srv://root:jinxisthebest@cluster0.1jnpn.mongodb.net/sample%95airbnb?retryWrites=true&w=majority")


def get(post_id): # getting an object from a database based on its id
 global client
 db = client.get_database('sample_airbnb')
 coll = db.get_collection('listingsAndReviews')
 post = coll.find_one({'_id': post_id})
 name = post['name'] # getting the name of the given object
 print(name) # printing the name

# Get user supplied values
filename = file.askopenfilename(initialdir="/Users/KAB-27-3/PycharmProjects/FaceRwithFile", title="Select file",
                                    filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
imagePath = filename
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # changed gray to rgb

detected = []
# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
)

if faces is not None:
    detected.append(faces)

print("Found {0} faces!".format(len(faces))) # printing how many faces are found
get("10006546") # getting a collection from database with this id

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    face = image[y: y + w, x: x + h]
    cv2.imwrite("foundface.jpg", face)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

faceFile = "0_face.jpg"
faceImage = face_recognition.load_image_file("0_face.jpg")
faceEncoding = face_recognition.face_encodings(faceImage)[0]

faceToCompareFile = "foundface.jpg"
faceToCompare = face_recognition.load_image_file("foundface.jpg")
faceToCompareEncoding = face_recognition.face_encodings(faceToCompare)[0]

results = face_recognition.compare_faces([faceEncoding], faceToCompareEncoding)

print(results)

for face in detected:
    i = 0
    add = str(i)
    #cv2.imwrite(add+"_face.jpg", image[y: y + w, x: x + h]) # saving found face to file
    i += 1

cv2.imshow("Faces found", image) # displaying the face
cv2.waitKey(0)