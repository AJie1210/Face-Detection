import cv2


#臉部偵測
case_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
faceDetected = cv2.CascadeClassifier(case_path)

image = cv2.imread('pic\\pic7.jpg')
image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
image_face = faceDetected.detectMultiScale(image, scaleFactor = 1.1, minNeighbors = 2, minSize = (30, 30), flags = cv2.CASCADE_SCALE_IMAGE)

#顯示臉部偵測數量
image_height = image.shape[0]
image_width = image.shape[1]
cv2.putText(image, "Found " + str(len(image_face)) + " face !", (10, image_height-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

#框選臉部
count = 1
for(x, y, w, h) in image_face:
    cv2.rectangle(image, (x, y), (x+w, y+h),(128, 255 , 0), 2)
    #擷取臉部
    filename = "pic_copy\\image_" + str(count) + ".jpg"
    image1 = image[y: y + h, x: x + w]
    image1 = cv2.resize(image1, (400, 400))
    cv2.imwrite(filename, image1)
    count = count + 1


cv2.imshow("Facedetected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
