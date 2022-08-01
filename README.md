# Opencv
 opencv

Face detection
{
    偵測特徵檔路徑:
    case_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

    偵測物件方法:
    {
       faceDetected = cv2.CascadeClassifier(case_path)

        detectMultiScale(#圖片-image, #偵測原理-scaleFactor = 1.1, #誤檢率參數-minNeighbors = 3, #最小偵測區塊-minSize = (10, 10), #檢測模式-flags = cv2.CASCADE_SCALE_IMAGE) 
    }

    臉部框選與擷取:
    {
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
    }
}
Create Canvas
{
    Canvas = numpy.ones | zeros((height, width, 3#BGR | 1#GRAY), numpy.uint8)
    numpy.ones #陣列元素初值 = 1 numpy.zeros #陣列元素初值 = 0
    numpy.uint8 #8bit integer

    Canvas[:] = (B, G, R) #畫布顏色
}
