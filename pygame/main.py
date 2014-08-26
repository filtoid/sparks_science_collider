import os, sys, uuid, pygame
from PIL import Image, ImageFilter

import pprint

def unique_id():
	return uuid.uuid4().__str__()

def delete(file_name):
	os.unlink(file_name)

def draw_image_to_screen(img=0):
	#fill screen black so the last image doesn't show.
	screen.fill((0,0,0))
	if img == 0:
		screen.blit(aryimg[curimg][0],(0,0))
	else:
		screen.blit(pygame.image.load(img),(0,0))
	pygame.display.flip()
	pass
	
def thumbnail():
	size = (128, 128)
	file_name = unique_id() + ".jpg"
	current_image = current_dir + "/" + aryimg[curimg][1].__str__()
	try:
		im =  Image.open(current_image)
	except:
		pprint.pprint("Unable to load image")

	im.thumbnail(size)
	im.save(file_name)
	return file_name

def zoom():
	file_name = "zoom" + unique_id() + ".jpg"
	current_image = current_dir + "/" + aryimg[curimg][1].__str__()
	try:
		im =  Image.open(current_image)
	except:
		pprint.pprint("Unable to load image")

	width, height = im.size
	new_size = (int((width * MAX_ZOOM) * (ZOOM_STEP / ZOOM_STEPS)), int((height * MAX_ZOOM) * (ZOOM_STEP / ZOOM_STEPS)))
	pprint.pprint(new_size)

	new_image = im.resize(new_size)
	new_image = new_image.crop((0,0,1024,1024))
	new_image.save(file_name)
	return file_name

def blur():
	file_name = "zoom" + unique_id() + ".jpg"
	current_image = current_dir + "/" + aryimg[curimg][1].__str__()
	try:
		im =  Image.open(current_image)
	except:
		pprint.pprint("Unable to load image")

	blurred = im.filter(ImageFilter.BLUR)
	blurred.save(file_name)
	return file_name


def get_files(directory, extension):
	image_array = []
	for file in os.listdir(directory):
		if file.endswith(extension):
			image_array.append(file)
	return image_array

pygame.init()

w = 1024
h = 1024
size=(w,h)
screen = pygame.display.set_mode(size)

current_dir = os.path.dirname(os.path.realpath(__file__))
images = get_files(current_dir, ".jpg")
total_images = images.__len__()
MAX_IMG = total_images - 1

aryimg = []
for image in images:
	image_data = [pygame.image.load(image), image]
	aryimg.append(image_data)
curimg = 0

ZOOM_STEP = 1
ZOOM_STEPS = 20
MIN_ZOOM = 1
MAX_ZOOM = 10

draw_image_to_screen()

Quit = False

while Quit is not True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				Quit = True

			elif event.key == pygame.K_a:
				curimg -= 1
				if curimg < 0:
					curimg = MAX_IMG-1
				draw_image_to_screen()
				ZOOM_STEP = 1

			elif event.key == pygame.K_d:
				curimg += 1
				if curimg > MAX_IMG-1:
					curimg = 0
				draw_image_to_screen()
				ZOOM_STEP = 1

			elif event.key == pygame.K_w:
				ZOOM_STEP += 1
				img = zoom()
				draw_image_to_screen(img)
				delete(current_dir + "/" + img)

			elif event.key == pygame.K_s:
				ZOOM_STEP -= 1
				img = zoom()
				draw_image_to_screen(img)
				delete(current_dir + "/" + img)

			elif event.key == pygame.K_x:
				draw_image_to_screen()
				ZOOM_STEP = 1

			elif event.key == pygame.K_b:
				img = blur()
				draw_image_to_screen(img)