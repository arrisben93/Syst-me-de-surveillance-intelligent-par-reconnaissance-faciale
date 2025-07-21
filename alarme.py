import pygame

pygame.init()
pygame.mixer.init()
alerte = pygame.mixer.Sound('alert.wav')

def declencher_alarme():
    alerte.play()
