from reconnaissance import detecter_visage
from base_donnees import initialiser_bdd, enregistrer_detection
from alarme import declencher_alarme

import cv2

if __name__ == "__main__":
    initialiser_bdd()
    capture = cv2.VideoCapture(0)
    while True:
        reponse, image = capture.read()
        if not reponse:
            break
        nom = detecter_visage(image)
        enregistrer_detection(nom)
        if nom == "Inconnu":
            declencher_alarme()
        cv2.imshow('Surveillance IA2', image)
        if cv2.waitKey(5) == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()
