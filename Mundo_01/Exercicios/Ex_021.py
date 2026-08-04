# Faça um programa em Python que abra e reproduza o aúdio de um arquivo MP3
# ((Aula 08))

import pygame

pygame.init()
pygame.mixer.music.load('Ex_021.mp3')
pygame.mixer.music.play()
pygame.event.wait()