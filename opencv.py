import cv2
import numpy

"""cv2.namedWindow("Image_1", flags=cv2.WINDOW_FREERATIO)"""
img_1 = cv2.imread('pic\\pic1.jpg')
img_1 = cv2.resize(img_1, (900, 600))
cv2.rectangle(img_1, (0, 0), (300, 300), (0, 0, 255), 3)
cv2.putText(img_1, "Wayne", (500, 50), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0 ,0), 2)
cv2.imshow("Image_1", img_1)
cv2.imwrite('pic_copy\\pic1_copy.jpg', img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()