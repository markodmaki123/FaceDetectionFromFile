import cv2
import tkinter.filedialog as file
from pymongo import MongoClient
from bson.objectid import ObjectId


client = MongoClient("mongodb+srv://root:jinxisthebest@cluster0.1jnpn.mongodb.net/sample%95airbnb?retryWrites=true&w=majority")

def get(post_id):
 global client
 db = client.get_database('sample_airbnb')
 coll = db.get_collection('listingsAndReviews')
 post = coll.find_one({'_id': post_id})
 name = post['name']
 print(name)

# Get user supplied values
filename = file.askopenfilename(initialdir="/Users/KAB-27-3/PycharmProjects/FaceRwithFile", title="Select file",
                                    filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"), ("png files", "*.png")))
imagePath = filename
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

print("Found {0} faces!".format(len(faces)))
get("10006546")

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

for face in detected:
    i = 0
    add = str(i)
    cv2.imwrite(add+"_face.jpg", gray[y: y + w, x: x + h])
    i += 1

cv2.imshow("Faces found", image)
cv2.waitKey(0)
