import cv2 as cv
# opencvと顔認識の準備
# Classifierというメソッドにxmlファイルを読み込む
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

img = cv.imread('photo-py.jpeg')

# grayイメージを作る
gray = cv.cvtColor(img,cv.COLOR_BG2GRAY)

4;00