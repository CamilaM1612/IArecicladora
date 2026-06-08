import cv2

cap = cv2.VideoCapture(0)

contador = 0

while True:
    ret, frame = cap.read()

    cv2.imshow("Captura", frame)

    tecla = cv2.waitKey(1)

    if tecla == ord('s'):
        cv2.imwrite(
            f"dataset/botella/img_{contador}.jpg",
            frame
        )
        contador += 1

    if tecla == 27:
        break

cap.release()
cv2.destroyAllWindows()