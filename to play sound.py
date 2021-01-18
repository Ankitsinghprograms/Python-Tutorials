#import pygame

#import time

#pygame.init()

#a=pygame.mixer.Sound("/storage/emulated/0/MIUI/sound_recorder/python.mp3")

#a.play()
#time.sleep(10)


#Second way


import time

from pygame import mixer
mixer.init()
mixer.music.load("/storage/emulated/0/none.mp3")
mixer.music.play()
time.sleep(60)
