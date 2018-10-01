import cv2, sys
import numpy as np

mirror = True

video_capture = cv2.VideoCapture(0)

height = 240
width = 320
half = int(width/2)
if mirror:
    blank_image = np.zeros((height, width+width, 3), np.uint8)
else:
    blank_image = np.zeros((height, width+half, 3), np.uint8)
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    small = cv2.resize(frame, (width, height) )
    if mirror:
        blank_image[0:height, half+1:width] = blank_image[0:height, half:width-1]
        blank_image[0:height, width:width+half-1] = blank_image[0:height, width+1:width+half]
        blank_image[0:height, half] = small[0:height, half]
        blank_image[0:height, width+half-1] = small[0:height, half]
        blank_image[0:height, 0:half] = small[0:height, 0:half]
        blank_image[0:height, width+half:width+width] = small[0:height, half:width]
    else:
       blank_image[0:height, half+1:width+half] = blank_image[0:height, half:width+half-1]
       blank_image[0:height, half] = small[0:height, half]
       blank_image[0:height, 0:half] = small[0:height, 0:half]

    cv2.imshow('hi i am a sunflower', blank_image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

