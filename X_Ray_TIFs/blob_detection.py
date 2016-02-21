import numpy as np
import cv2
from matplotlib import pyplot as plt
from PIL import Image,ImageDraw
import cv2.cv as cv


im = cv2.imread('/home/alex/Spark/images/image11.TIFF',cv2.IMREAD_GRAYSCALE)
im_compressed = cv2.imread('/home/alex/Spark/images_out/image11.TIFF',cv2.IMREAD_GRAYSCALE)

detector = cv2.SimpleBlobDetector()

keypoints = detector.detect(im)
keypoints_compressed = detector.detect(im_compressed)

image = Image.open('/home/alex/Spark/images/image11.TIFF')
image_compressed = Image.open('/home/alex/Spark/images_out/image11.TIFF')
draw = ImageDraw.Draw(image)
draw_compressed = ImageDraw.Draw(image_compressed)
for i in range(min(len(keypoints),len(keypoints_compressed))):
    x = keypoints[i].pt[0]
    y = keypoints[i].pt[1]
    x_compressed = keypoints_compressed[i].pt[0]
    y_compressed = keypoints_compressed[i].pt[1]
    draw.ellipse((x-100,y-100,x+100,y+100),outline='red')
    draw_compressed.ellipse((x_compressed-100,y_compressed-100,x_compressed+100,y_compressed+100),outline='red')

image.save('/home/alex/Spark/images/image11_circles.TIFF')
image_compressed.save('/home/alex/Spark/images_out/image11_circles_compressed.TIFF')
