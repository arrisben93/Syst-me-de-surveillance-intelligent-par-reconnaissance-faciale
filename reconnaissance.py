import cv2
import numpy as np
import face_recognition

signatures = np.load('SignaturesAll.npy', allow_pickle=True)
encodages = signatures[:, :-1].astype('float')
noms = signatures[:, -1]

def detecter_visage(image):
    image_reduit = cv2.resize(image, (0, 0), None, 0.25, 0.25)
    emplacements = face_recognition.face_locations(image_reduit)
    encodes = face_recognition.face_encodings(image_reduit, emplacements)
    nom_detecte = "Inconnu"
    for encode, loc in zip(encodes, emplacements):
        matches = face_recognition.compare_faces(encodages, encode)
        distances = face_recognition.face_distance(encodages, encode)
        index_min = np.argmin(distances)
        y1, x2, y2, x1 = loc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
        couleur = (0, 255, 0) if matches[index_min] else (0, 0, 255)
        nom_detecte = noms[index_min] if matches[index_min] else "Inconnu"
        cv2.rectangle(image, (x1, y1), (x2, y2), couleur, 2)
        cv2.putText(image, nom_detecte, (x1, y2+25), cv2.FONT_HERSHEY_SIMPLEX, 1, couleur, 2)
    return nom_detecte
