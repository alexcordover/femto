import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image,ImageDraw
import cv2.cv as cv


im = cv2.imread('/home/alex/Spark/images/image11.TIFF',cv2.IMREAD_GRAYSCALE)
'''
im_copy = im.copy()
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray,cv.CV_HOUGH_GRADIENT,1.2,100)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles:
        cv2.circle(im_copy, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(im_copy, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    cv2.imshow("im_copy", np.hstack([im, im_copy]))
    cv2.waitKey(0)
else:
    print('No circles')

'''
detector = cv2.SimpleBlobDetector()

keypoints = detector.detect(im)
print(len(keypoints))

image = Image.open('/home/alex/Spark/images/image11.TIFF')
draw = ImageDraw.Draw(image)
for i in range(10):
    x = keypoints[i].pt[0]
    y = keypoints[i].pt[1]
    print((x,y))
    draw.ellipse((x-100,y-100,x+100,y+100))

image.save('/home/alex/Spark/images/image11_cirlces.TIFF')

#im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#cv2.imshow("Keypoints",im_with_keypoints)
#cv2.waitKey(0)
