#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Victor Nieves Sanchez"
__copyright__ = "Copyright 2018, Victor Nieves Sanchez"
__credits__ = ["Victor Nieves Sanchez"]
__license__ = "GPL"
__version__ = "1.0.1"
__python__= "3.6.4"
__email__ = "vnievess@gmail.com"

import backend
from colors import color
import sys

class Game(object):
	def __init__(self):
		name = ""
		item = ""
		lastAnswer = ""
		world = ""

def checkPyVersion():
	if sys.version_info < (3,0):
		print(color("Por favor use la version 3.0 o superior", fg= 'red', style= 'bold'))
		sys.exit(1)

def loading():
	backend.sayToUser(color(".CARGANDO ENTORNO.", fg='green'))
	backend.sleep(0.5)
	backend.sayToUser(color(".                .", fg ='green'))
	backend.sleep(1)
	backend.sayToUser(color("..              ..", fg ='green'))
	backend.sleep(0.6)
	backend.sayToUser(color("...            ...", fg ='green'))
	backend.sleep(1)
	backend.sayToUser(color("....          ....", fg ='green'))
	backend.sleep(0.5)
	backend.sayToUser(color(".....        .....", fg ='green'))
	backend.sleep(0.5)
	backend.sayToUser(color("......      ......", fg ='green'))
	backend.sleep(1)
	backend.sayToUser(color(".......    .......", fg ='green'))
	backend.sleep(1)
	backend.sayToUser(color("........  ........", fg= 'green'))
	backend.sleep(0.5)
	backend.sayToUser(color("..................", fg= 'green'))
	backend.sleep(0.5)
	backend.sayToUser(color("..................", fg= 'green'))
	backend.sleep(0.5)
	checkPyVersion()
	backend.sayToUser(color("....INICIANDO.....", fg ='green'))
	backend.sleep(1)
	backend.sayToUser(color("..................", fg= 'green'))
	backend.sleep(0.7)

def intro():
	backend.sayToUser("Son las 05:00AM, estás en un garito de mala muerte con tus colegas y vas algo “feliz”.")
	backend.sleep(1.5)
	backend.sayToUser("Te quieres ir a casa. Y ¿Qué harás? ...")
	backend.sleep(1)
	answer = backend.askToUser("1) Le dices a tus colegas que ya te marchas.\n2) Haces bomba de humo.")
	while (answer != "1") and (answer != "2"):
		backend.nonValidAnswer()
		answer = backend.askToUser("1) Le dices a tus colegas que ya te marchas.\n2) Haces bomba de humo.")
	backend.sayToUser("De camino a casa te encuentras con una persona encapuchada. No consigues ver su cara.")
	backend.sleep(1.5)
	backend.sayToUser("El te habla:")
	backend.sleep(1)
	backend.sayDialogue("- ¡Ey! Joven, ¿quieres fumar del porro?")
	backend.sleep(1)
	backend.sayToUser("Te ofrece un porro. ¿Lo aceptas?")
	answer = backend.askToUser("1) Si.\n2) No.")
	while (answer != "1") and (answer != "2"):
		backend.nonValidAnswer()
		answer = backend.askToUser("1) Si.\n2) No.")
	return answer

def badEnding():
	backend.sayDialogue("- ¡¿COOOOOMOO?! Vaya gilipollas eres. ¡Ala, a mamarla!")
	backend.sleep(1.1)
	backend.sayToUser("Sigues caminando de camino a casa. Consigues a duras penas llegar a tu cama.")
	backend.sleep(1.3)
	backend.sayToUser("Te tumbas y te duermes.")
	backend.sleep(2)
	backend.sayToUser(".")
	backend.sleep(1)
	backend.sayToUser("..")
	backend.sleep(1)
	backend.sayToUser("...")
	backend.sleep(1)
	backend.sayToUser(color("FIN",fg = 'blue', style = 'bold+underline'))
	backend.sleep(2)
	sys.exit(0)

def continuation1():
		backend.sayDialogue("- Toma toma, a disfrutarlo. (Te da el porro y se va haciendo la croqueta).")
		backend.sleep(1)
		backend.sayToUser(".")
		backend.sleep(1)
		backend.sayToUser("..")
		backend.sleep(1)
		backend.sayToUser("...")
		backend.sleep(1)
		backend.sayToUser("Llegas a tu casa a duras penas. Te comes un güen bocadillo de lomo puta madre.")
		backend.sleep(1)
		backend.sayToUser("Te bebes un vasito de leche con Nesquick.")
		backend.sleep(1)
		backend.sayDialogue("(PORQUE EL  COLACAO ES UNA PUTA MIERDA)")
		backend.sleep(0.7)
		backend.sayToUser("Te vas a la cama y te duermes ipso facto.")
		backend.sleep(1)
		backend.sayToUser(".")
		backend.sleep(1)
		backend.sayToUser("..")
		backend.sleep(1)
		backend.sayToUser("...")
		backend.sleep(1)
		backend.sayToUser("Ya es de día.")
		backend.sleep(0.5)
		backend.sayToUser("Te despiertas en una habitación, pero no es la tuya. ")
		backend.sleep(1)
		backend.sayDialogue("¿Dónde coño te acostaste anoche? ¿Era tu casa?")
		backend.sleep(1)
		backend.sayToUser("Como sea. Te pones a mirar a tu alrededor.") 
		backend.sleep(1)
		backend.sayToUser("Ves lo que parece una cabina britanica de policía azul.")
		backend.sleep(1)
		backend.displayImage("Cabina extraña.", "images/Dwho.jpg")
		backend.sleep(1)
		backend.sayToUser("¿Entras en la máquina?")
		answer = backend.askToUser("1) Si.\n2) No.")
		while (answer != "1") and (answer != "2"):
			backend.nonValidAnswer()
			answer = backend.askToUser("1) Si.\n2) No.")
		return answer

def insertName():
	return backend.askToUser("Te pide que introduzcas tu nombre:")
	
def choseWorld():
	backend.sayToUser("Ves que hay una serie de destinos disponibles.")
	backend.sleep(0.5)
	backend.sayToUser("El mundo de la bella y la bestia, Dubai, el puticlub Las Flores, Nuevo Londo . . . ")
	backend.sleep(1.5) 
	backend.sayToUser("Eliges un destino.")
	backend.sleep(0.5)
	answer = backend.askToUser("1) El mundo de la bella y la bestia.\n2) Dubai.\n3) El puticlub Las Flores.\n4) Nuevo Londo.")
	while (answer != "1") and (answer != "2") and (answer != "3") and (answer != "4"):
			backend.nonValidAnswer()
			answer = backend.askToUser("1) El mundo de la bella y la bestia.\n2) Dubai.\n3) El puticlub Las Flores.\n4) Nuevo Londo.")
	if answer == "1":
		world = "El mundo de la bella y la bestia"
	elif answer == "2":
		world = "Dubai"
	elif answer == "3":
		world = "El puticlub Las Flores"
	else:
		world = "Nuevo Londo"
	backend.sayToUser("Eliges como destino " + world + ".")
	return world
		
def main():
	try:
		gameData = Game()
		loading()
		gameData.lastAnswer = intro()
		if gameData.lastAnswer == "2":
			badEnding()
			sys.exit(0)	
		else:
			gameData.lastAnswer = continuation1()
			if gameData.lastAnswer == '2':		
				backend.sayDialogue("- !Pero vamos a ver, gilí!¿Qué eres león o güevón?. Entras igual porque así lo quiero yo.")
				backend.sleep(1.3)
			backend.sayToUser("Entras en la máquina.")		
			gameData.name = insertName()
			backend.sleep(0.5)
			gameData.world = choseWorld()
			backend.sleep(0.5)
			print("CONTINUA")
			#pero de repente escuchas...
	except KeyboardInterrupt:
		backend.keyboardInterruptText()
if __name__ == "__main__":
	main()


