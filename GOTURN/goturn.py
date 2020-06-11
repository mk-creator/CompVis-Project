from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import time
import cv2
import sys, os

tracker = cv2.TrackerGOTURN_create()

initBB = None

#Replace 'test_vid.mp4' with name of video desired
vs = cv2.VideoCapture('test_vid.mp4')
fps = None
counter = 1

while True:
    ret, frame = vs.read()

    if frame is None:
        break

    frame = imutils.resize(frame, width=700)
    (H, W) = frame.shape[:2]
    
    if initBB is not None:
        (success, box) = tracker.update(frame)

        if success:
            (x, y, w, h) = [int(v) for v in box]
            # cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 255, 0), 2)

        fps.update()
        fps.stop()

        if counter % 10 == 0:
            print(fps.fps())
            cv2.rectangle(frame, (x, y), (x + w, y + h),(0, 255, 0), 2)
            cv2.imshow("Frame", frame)


        counter = counter + 1

    key = cv2.waitKey(1) & 0xFF
    
    if initBB is None:
        cv2.imshow("Frame", frame)

    if key == ord("s"):
        initBB = cv2.selectROI("Frame", frame, fromCenter=False,showCrosshair=True)
        tracker.init(frame, initBB)
        fps = FPS().start()

    elif key == ord("q"):
        break

vs.release()
cv2.destroyAllWindows()
