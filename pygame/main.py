import sys, pygame
import time


def draw_image_to_screen():
	screen.blit(aryimg[curimg],(0,0))
	pygame.display.flip()
	pass

pygame.init()

w = 1024
h = 1024
size=(w,h)
screen = pygame.display.set_mode(size)

MAX_IMG = 21

img=pygame.image.load('9.jpg')
aryimg = []
for i in range(0, MAX_IMG):
	aryimg.append( pygame.image.load( str(i+1) + '.jpg') )

curimg = 0
draw_image_to_screen()

Quit = False

while Quit is not True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
				Quit = True
			elif event.key == pygame.K_a:
				curimg -= 1
				if curimg < 0:
					curimg = MAX_IMG-1
				draw_image_to_screen()
			elif event.key == pygame.K_d:
				curimg += 1
				if curimg > MAX_IMG-1:
					curimg = 0
				draw_image_to_screen()