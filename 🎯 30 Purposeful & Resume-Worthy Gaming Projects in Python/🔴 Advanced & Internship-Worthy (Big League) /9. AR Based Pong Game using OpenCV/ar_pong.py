# ar_pong.py
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ball_pos = np.array([320,240], dtype=float)
velocity = np.array([4.0, 3.0])
radius = 15

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame,1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # assume green paddle: tune ranges
    lower = np.array([40, 70, 70])
    upper = np.array([80, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    paddle_x = None
    if contours:
        c = max(contours, key=cv2.contourArea)
        x,y,w,h = cv2.boundingRect(c)
        paddle_x = x + w//2
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    # move ball
    ball_pos += velocity
    # bounce walls
    if ball_pos[1] <= radius or ball_pos[1] >= frame.shape[0]-radius:
        velocity[1] *= -1
    # check paddle collision (right side)
    if paddle_x and abs(ball_pos[0] - paddle_x) < 50 and ball_pos[0] > frame.shape[1]-200:
        velocity[0] *= -1
    cv2.circle(frame, tuple(ball_pos.astype(int)), radius, (0,0,255), -1)
    cv2.imshow("AR Pong", frame)
    if cv2.waitKey(1) & 0xFF == 27: break
cap.release(); cv2.destroyAllWindows()
