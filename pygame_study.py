import pygame

import time

from pygame import mixer

pygame.init()

width=400
height=400

screen=pygame.display.set_mode((width,height))

background=pygame.image.load("background.png").convert()

background=pygame.transform.scale(background,(720,1370))

water_image=pygame.image.load("water.jpg")

water=pygame.transform.scale(water_image,(400,400))

font=pygame.font.SysFont(None,100)

text=font.render("You clicked",True,(0,0,0))

#My phone size height-1370px and width-720px

mouse_key=pygame.mouse.get_pressed()


#image = pygame.image.load('/storage/emulated/0/Python/Tutorials/file1.jpg') 

#image = pygame.transform.scale(image, (720,1370)) #trasfoem size of image

def sound(n):

	mixer.init()
	mixer.music.load(n)
	mixer.music.play(-1)
	time.sleep(3)

done=False

while True:
	
	screen.blit(background,(0,0))
	
	mouse=pygame.mouse.get_pos()#mouse position in while so its chages everytime and give accurate data
	
#	screen.fill((255,0,255))
	screen.blit(water,(160,300))
	
	
	if 200<mouse[0]<400 and 200<mouse[1]<400: #mouse[0]=x axis and mouse[1]=y axis

		a=pygame.draw.rect(screen,(255,0,0),(200,200, 200, 200))
		
		screen.blit(text,(100,100))
		
		sound("water.mp3")
		
	else:
		
		mixer.music.stop()
		a=pygame.draw.rect(screen,(0,0,0),(200, 200, 200, 200))
		
	
#	screen.blit(image,(0,0)) #To show image and then place of that(x axis,y axis)
	
#	screen.blit(a,(0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done=True
		
	
	pygame.display.update()


#pygame.display.flip()
