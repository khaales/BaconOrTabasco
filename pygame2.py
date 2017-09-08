import pygame, time
from random import randint
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


x = 0
y = 0
x_coord = 350
y_coord = 250


bg = pygame.image.load("grass.jpg")
bg = pygame.transform.scale(bg, (800,800))

pig = pygame.sprite.Sprite()
pig.image = pygame.image.load("pig.png")
pig.image = pygame.transform.scale(pig.image, (70,70))
pig.rect = pig.image.get_rect()
pig_group = pygame.sprite.GroupSingle(pig)
#pig_group = pygame.sprite.OrderedUpdates()

#food = pygame.sprite.Group()
food = pygame.sprite.OrderedUpdates()
for i in range(5):
	bacon = pygame.sprite.Sprite()
	bacon.image = pygame.image.load("bacon3.png")
	bacon.image = pygame.transform.scale(bacon.image, (50,50))
	bacon.rect = bacon.image.get_rect()
	x_bacon = randint(10,750)
	y_bacon = randint(10,550)
	bacon.rect.x = x_bacon 
	bacon.rect.y = y_bacon 
	food.add(bacon)

enemy = pygame.sprite.OrderedUpdates()
#enemy = pygame.sprite.Group()
#sauce = pygame.sprite.Sprite()
#def add_sauce(enemy):
#	sauce.image = pygame.image.load("hotsauce.png")
#	sauce.image = pygame.transform.scale(sauce.image, (35, 80))
#	sauce.rect = sauce.image.get_rect()
#	x_sauce = randint(10,650)
#	y_sauce = randint(10,450)
#	sauce.rect.x = x_sauce
#	sauce.rect.y = y_sauce 
#	enemy.add(sauce)


for i in range(2):
	sauce = pygame.sprite.Sprite()
	sauce.image = pygame.image.load("hotsauce.png")
	sauce.image = pygame.transform.scale(sauce.image, (35,80))
	sauce.rect = sauce.image.get_rect()
	x_sauce = randint(10,440) or randint(460, 850)
	y_sauce = randint(10,340) or randint(360, 650)
	sauce.rect.x = x_sauce 
	sauce.rect.y = y_sauce 
	enemy.add(sauce)	

pygame.init()


# Set the width and height of the screen [width, height]
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Feed the Pig!")
running = True
win = False
lose = False

clock = pygame.time.Clock()
pygame.mouse.set_visible(0)
pygame.time.set_timer(pygame.USEREVENT, 2000)


# -------- Main Program Loop -----------
while running:
	x_coord += x
	y_coord += y
	
	screen.fill(WHITE)
	pig.rect.x = x_coord 
	pig.rect.y = y_coord 

	screen.blit(bg, (0, 0))
	pig_group.draw(screen)
	food.draw(screen)
	enemy.draw(screen)
   
	 # --- Main event loop
	for event in pygame.event.get():
		if (event.type == pygame.QUIT) or (event.type == pygame.K_c):
			running = False
			pygame.display.quit()
		

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x = -3
			elif event.key == pygame.K_RIGHT:
				x = 3
			elif event.key == pygame.K_UP:
				y = -3
			elif event.key == pygame.K_DOWN:
				y = 3
 
        # User let up on a key
		elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				x = 0
			elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				y = 0
		if event.type == pygame.USEREVENT:
			if win == False or lose == False:
				for i in range(2):
					#add_sauce(enemy)
					sauce = pygame.sprite.Sprite()
					sauce.image = pygame.image.load("hotsauce.png")
					sauce.image = pygame.transform.scale(sauce.image, (35,80))
					sauce.rect = sauce.image.get_rect()
					x_sauce = randint(10, 850)
					y_sauce = randint(10, 650)
					sauce.rect.x = x_sauce 
					sauce.rect.y = y_sauce 
					enemy.add(sauce)					
				#enemies.append(enemy(sauce) for x in range(10))
				#enemy.add(sauce)
				#enemy.draw(screen)
				#pygame.display.update()
	
	pygame.sprite.groupcollide(pig_group, food, False, True)
	collide = pygame.sprite.spritecollideany(pig, enemy)

	if len(food) == 0:
		win = True
	if win:
		font = pygame.font.Font(None, 100)
		text_image = font.render("You WIN!!", True, GREEN)
		screen.blit(text_image, (200, 200))
		restart = font.render('Restart? y/n', True, BLACK)
	 	screen.blit(restart, (200,300))

	
	if collide:
		lose = True
	if lose:
		font = pygame.font.Font(None, 100)
		text_image = font.render("You LOSE!!", True, RED)
		screen.blit(text_image, (200, 200))
		restart = font.render('Restart? y/n', True, BLACK)
	 	screen.blit(restart, (200,300))
	
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_n:
			pygame.display.quit()
			pygame.quit()
			running = False
		elif event.key == pygame.K_y:
			exec file('pygame2.py')
	
	pygame.display.flip()
	pygame.display.update()
	clock.tick(60)


# Close the window and quit.
pygame.quit()
