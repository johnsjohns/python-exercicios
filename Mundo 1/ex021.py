import pygame
pygame.mixer.init()
pygame.mixer.music.load('Mundo 1/Som/Som.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()