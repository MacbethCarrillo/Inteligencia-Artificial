import cv2
import os
import numpy as np

dataPath = 'C:/Users/windows 11/Desktop/ReconocimientoFacial/Data'  # Cambia a la ruta donde hayas almacenado Data
peopleList = os.listdir(dataPath)
print('Lista de personas:', peopleList)

labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = os.path.join(dataPath, nameDir)
    print('Leyendo las imágenes de', nameDir)

    for fileName in os.listdir(personPath):
        print('Rostros:', nameDir + '/' + fileName)
        labels.append(label)
        imagePath = os.path.join(personPath, fileName)
        faceImage = cv2.imread(imagePath, 0)
        facesData.append(faceImage)

    label += 1

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

modeloPath = os.path.join(dataPath, 'modeloLBPHFace.xml')
face_recognizer.write(modeloPath)
print("Modelo almacenado en", modeloPath)
