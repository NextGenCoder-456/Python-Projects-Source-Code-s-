import cv2
import face_recognition
import os
from datetime import datetime

# Load images from known_faces directory
path = 'known_faces'
images = []
classNames = []
for filename in os.listdir(path):
    img = cv2.imread(f'{path}/{filename}')
    images.append(img)
    classNames.append(os.path.splitext(filename)[0])

# Encode all known images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encodeList.append(face_recognition.face_encodings(img)[0])
    return encodeList

# Mark attendance to a CSV
def markAttendance(name):
    with open('Attendance.csv', 'a+') as f:
        f.seek(0)
        lines = f.readlines()
        if name not in [line.split(',')[0] for line in lines]:
            dt = datetime.now().strftime('%H:%M:%S, %d-%m-%Y')
            f.write(f'{name},{dt}\n')

encodeListKnown = findEncodings(images)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    small = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)
    rgb = cv2.cvtColor(small, cv2.COLOR_BGR2RGB)

    faces = face_recognition.face_locations(rgb)
    encodes = face_recognition.face_encodings(rgb, faces)

    for encode, faceLoc in zip(encodes, faces):
        matches = face_recognition.compare_faces(encodeListKnown, encode)
        name = "Unknown"
        if True in matches:
            idx = matches.index(True)
            name = classNames[idx].upper()
            markAttendance(name)
        y1, x2, y2, x1 = [v * 4 for v in faceLoc]
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(img, name, (x1,y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == 27:  # ESC to break
        break

cap.release()
cv2.destroyAllWindows()
