import pygame
import time

pygame.init()
running = True

events = pygame.event.get()

keys=pygame.key.get_pressed()

while running:
	print "hello world"
	time.sleep(1)
	for event in events:
		if event.key == pygame.K_DELETE:
			running = False