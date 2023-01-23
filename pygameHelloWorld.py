import pygame, sys

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
FPS = 60
pygame.display.set_caption('Hello World!')
clock = pygame.time.Clock()

while True: # main game loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		print(event)
	
	pygame.display.update()
	clock.tick(FPS)