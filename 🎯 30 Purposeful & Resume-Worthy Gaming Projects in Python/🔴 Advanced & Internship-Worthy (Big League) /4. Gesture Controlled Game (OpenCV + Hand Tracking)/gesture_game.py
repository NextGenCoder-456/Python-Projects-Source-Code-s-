# gesture_game.py
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
width = 640; height = 480

while True:
    ret, frame = cap.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)
    cx = width//2; cy = height//2
    if res.multi_hand_landmarks:
        for lm in res.multi_hand_landmarks[0].landmark:
            pass
        # index finger tip is id=8
        idx = res.multi_hand_landmarks[0].landmark[8]
        cx = int(idx.x * width)
        cy = int(idx.y * height)
        mp_draw.draw_landmarks(frame, res.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)
    # draw controlled circle
    cv2.circle(frame, (cx, cy), 30, (0,255,0), -1)
    cv2.imshow("Gesture Game", frame)
    if cv2.waitKey(1) & 0xFF == 27: break
cap.release()
cv2.destroyAllWindows()
