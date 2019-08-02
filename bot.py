from PIL import ImageGrab, Image
import os
from time import sleep
from pyautogui import press, typewrite, hotkey, keyDown, keyUp

bbox = (0, 209, 800, 400)
colors = [0x0000ff, 0xff0000]
color = 0
speed = 0
prev_dist = 0

while True:
	im = ImageGrab.grab(bbox)
	im.save('tmp.png')
	width, height = im.size
	distance = 0
	bird_distance = 0
	avg = 0
	for x in range(10):
		avg += im.getpixel((x, 0))[0]
	avg //= 10
	iswhite = int(avg > 128) * 2 - 1
	for x in range(83, width):
		r, g, b = im.getpixel((x,163))
		if (r - 128) * iswhite < 0:
			distance = x
			break
	for x in range(83, width):
		r, g, b = im.getpixel((x,125))
		if (r - 128) * iswhite < 0:
			bird_distance = x
			break
	if distance - prev_dist < 100:
		speed = prev_dist - distance
	print(distance, '\t', bird_distance, '\t', speed)
	if distance < 110 + 1.5 * speed:
		press(' ')
	if bird_distance < 250:
		keyDown('down')
		sleep(0.5)
		keyUp('down')
	prev_dist = distance
	sleep(0.1)
