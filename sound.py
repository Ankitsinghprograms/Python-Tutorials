import time
import pygame
from pygame import mixer

def s(n):
	while True:
		mixer.init()
		mixer.music.load(n)
		mixer.music.play(-1)
		time.sleep(3)
#s("/storage/emulated/0/Python/Tutorials/Exercises/Healthy Programmer/eyes.mp3")