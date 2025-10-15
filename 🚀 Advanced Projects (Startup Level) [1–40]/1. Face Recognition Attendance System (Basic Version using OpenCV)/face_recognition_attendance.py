# face_recognition_attendance.py
import cv2
import numpy as np
import face_recognition
from datetime import datetime

# Load known images and encode them
known_face_encodings = []
known_face_names = ['Ankush', 'Piyush']

for name in known_face_names:
    img = face_recognition.load_image_file(f"{name}.jpg")
    known_face_encodings.append(face_recognition.face_encodings(img)[0])

# Start webcam
cap = cv2.VideoCapture(0)

def mark_attendance(name):
    with open('attendance.csv', 'a+') as f:
        now = datetime.now().strftime('%H:%M:%S')
        f.write(f'{name},{now}\n')

while True:
    ret, frame = cap.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(known_face_encodings, encoding)
        name = "Unknown"

        if True in matches:
            index = matches.index(True)
            name = known_face_names[index]
            mark_attendance(name)

        top, right, bottom, left = [v * 4 for v in location]
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255,255), 2)

    cv2.imshow('Attendance System', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
