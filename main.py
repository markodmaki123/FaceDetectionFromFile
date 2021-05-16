import cv2
import tkinter.filedialog as file

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
    scaleFactor=1.2,
    minNeighbors=5,
    minSize=(30, 30),
)

if faces is not None:
    detected.append(faces)

print("Found {0} faces!".format(len(faces)))

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
