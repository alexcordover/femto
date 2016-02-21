import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image,ImageDraw

im = cv2.imread('image5.jpg',cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector()

keypoints = detector.detect(im)
image = Image.open('image5.jpg')
draw = ImageDraw.Draw(image)
for i in range(10):
    x = keypoints[i].pt[0]
    y = keypoints[i].pt[1]
    print((x,y))
    draw.ellipse((x-25,y-25,x+25,y+25))

image.save('image5cirlces.jpg')

#im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.imshow("Keypoints",im_with_keypoints)
#cv2.waitKey(0)
