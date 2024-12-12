import pygame
pygame.init()
#300 500 700
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
X = 600
Y = 800
display_surface = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('B', True, green)
text1 = font.render('B', True, green)
text2 = font.render('B', True, green)	
textRect = text.get_rect()
textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect.center = (100, 400)
textRect1.center = (300, 400)
textRect2.center = (500, 400)
while True:
	display_surface.fill(white)
	display_surface.blit(text, textRect)
	display_surface.blit(text1, textRect1)
	display_surface.blit(text2, textRect2)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	pygame.display.update()