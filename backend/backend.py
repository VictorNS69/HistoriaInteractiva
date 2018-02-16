#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__AUTHOR__ = "Victor Nieves Sanchez"
__COPYRIGHT__ = "Copyright 2018, Victor Nieves Sanchez"
__CREDITS__ = ["Victor Nieves Sanchez"]
__LICENSE__ = "GPL"
__VERSION__ = "1.0.0"
__PYTHON__= "3.6.4"
__EMAIL__ = "vnievess@gmail.com"


import time
import pygame
from colors import color

def sayToUser(message):
	print(message)

def sayDialogue(message):
	print (color(message, style='italic'))

def askToUser(question):
	for item in question.split('\n'):
		print(color(item,style='bold'))
		sleep(1)
	return input()

def nonValidAnswer():
	print(color("¡Elige una opcion valida coño!", fg='red'))

def sleep(t):
	time.sleep(0) # 0 -> t 

def keyboardInterruptText():
	print("\n")
	print(color("¿Ya te vas?", fg="blue", style="bold"))
	sleep(1)
	byeInfo()

def byeInfo():
	print(color("Espero que te lo hayas pasado bien.", fg="blue", style="bold"))
	sleep(1.5)
	print(color("El autor:", fg="white", style="bold"))
	sleep(1)
	print(color("Victor Nieves Sanchez.", fg="blue", style="bold+italic+underline"))
	sleep(1)	

def displayImage(description, image):
	pygame.init()
	display_width = 800
	display_height = 600
	gameDisplay = pygame.display.set_mode((display_width, display_height))
	pygame.display.set_caption(description)
	black = (0, 0, 0)
	white = (255, 255, 255)
	img = pygame.image.load(image)
	gameDisplay.fill(white)
	gameDisplay.blit(img, (0, 0))
	pygame.display.update()
	#time.sleep(2)	
	sleep(2)
	pygame.quit()

