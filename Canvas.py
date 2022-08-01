from tkinter import N
import cv2
import numpy

Canvas = numpy.ones((800, 600, 3), numpy.uint8)
Canvas[:] = (255, 125, 125) 

cv2.imshow('Canvas', Canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()