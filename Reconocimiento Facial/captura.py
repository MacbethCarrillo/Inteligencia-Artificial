import cv2
import os
import imutils

personName = 'Gogo'
dataPath = 'C:/Users/windows 11/Desktop/ReconocimientoFacial/Data'
personPath = os.path.join(dataPath, personName)

os.makedirs(personPath, exist_ok=True)
print('Carpeta creada:', personPath)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0

while count < 10:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = imutils.resize(frame, width=640)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = frame.copy()

    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        rostro = auxFrame[y:y+h, x:x+w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(f'{personPath}/rostro_{count}.jpg', rostro)
        count += 1

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
