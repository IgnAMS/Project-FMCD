import cv2
import os

cam = cv2.VideoCapture("great.mp4")

try:
    os.remove('data')
except OSError:
    print("efe ;c")


os.makedirs('data')

curr_frame = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("curr frame", curr_frame)
        break
    if curr_frame % 15 == 0:
        name = f"./data/fream_{curr_frame // 15}.jpg"
        cv2.imwrite(name, frame)
    curr_frame += 1
