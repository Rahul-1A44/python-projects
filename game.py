# prompt: create box racing game

import pygame
import random

# Define the colors used in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the dimensions of the game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define the speed of the box
box_SPEED = 5

# Define the number of lanes on the way
NUM_LANES = 3

# Define the width of each lane
LANE_WIDTH = SCREEN_WIDTH / NUM_LANES

# Define the height of each box
box_HEIGHT = 50

# Define the width of each box
box_WIDTH = 25

# Define the starting position of the player's box
PLAYER_box_X = LANE_WIDTH * 1
PLAYER_box_Y = SCREEN_HEIGHT - box_HEIGHT

# Initialize the game engine
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dochhing game")

# Create a clock to track time
clock = pygame.time.Clock()

# Create a group to hold all the sprites in the game
all_sprites = pygame.sprite.Group()

# Create a group to hold the player's box
player_box_group = pygame.sprite.Group()

# Create a group to hold the enemy boxes
enemy_box_group = pygame.sprite.Group()

# Create the player's box
player_box = pygame.sprite.Sprite()
player_box.image = pygame.Surface((box_WIDTH, box_HEIGHT))
player_box.image.fill(BLUE)
player_box.rect = player_box.image.get_rect()
player_box.rect.x = PLAYER_box_X
player_box.rect.y = PLAYER_box_Y
player_box_group.add(player_box)
all_sprites.add(player_box)

# Create the enemy boxes
for i in range(10):
    enemy_box = pygame.sprite.Sprite()
    enemy_box.image = pygame.Surface((box_WIDTH, box_HEIGHT))
    enemy_box.image.fill(RED)
    enemy_box.rect = enemy_box.image.get_rect()
    enemy_box.rect.x = random.randint(0, SCREEN_WIDTH - box_WIDTH)
    enemy_box.rect.y = random.randint(-SCREEN_HEIGHT, 0)
    enemy_box_group.add(enemy_box)
    all_sprites.add(enemy_box)

# Initialize the score
score = 0
font = pygame.font.Font(None, 36)  # Set up the font for the score display

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the player's box
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_box.rect.x > 0:
        player_box.rect.x -= box_SPEED
    if keys[pygame.K_RIGHT] and player_box.rect.x < SCREEN_WIDTH - box_WIDTH:
        player_box.rect.x += box_SPEED

    # Update the enemy boxes
    for enemy_car in enemy_box_group:
        enemy_car.rect.y += box_SPEED
        if enemy_car.rect.y > SCREEN_HEIGHT:
            enemy_car.rect.y = random.randint(-SCREEN_HEIGHT, 0)
            enemy_car.rect.x = random.randint(0, SCREEN_WIDTH - box_WIDTH)
               #Inceament the score card by time
    score += 1

    # Check for collisions between the player's box and the enemy boxes
    collisions = pygame.sprite.spritecollide(player_box, enemy_box_group, True)
    if collisions:
        running = False
        
    

    # Draw the game screen
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Render the score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    

    # Update the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Quit the game
pygame.quit()
