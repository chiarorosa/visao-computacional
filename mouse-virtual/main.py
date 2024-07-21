import cv2
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    cv2.imshow('Deteccao de gesto para mexer o mouse', frame)
    cv2.waitKey(1)