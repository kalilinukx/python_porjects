import pygame
import random

# initialising of pygame
pygame.init()
# create game window
screen = pygame.display.set_mode((800, 600))
# background
background = pygame.image.load('background.png')
# create the Title and icon
pygame.display.set_caption("Space Invadors")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 380
playerX_change = 0
# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40
# Bullet
# ready- you can't see the bullets on the screen
# fire - the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullets(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x, y+10))
# Game loop


running = True
while running:
    #         standard for RGB red,green, blue
    screen.fill((0, 0, 0))
    # background image
    screen.blit(background, (0, 0))
    # playerY -= 0.07
    player(playerX, playerY)
    enemy(enemyX, enemyY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= -5
            if event.key == pygame.K_RIGHT:
                playerX_change -= +5
            if event.key == pygame.K_SPACE:
                fire_bullets(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
#    8=8+-0.1->=5-0.1
#    8=8+0.1
# checking for boundaries  of spaceship so it doesn't go out of boundaries
    playerX += playerX_change
    if playerX < 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
# Enemy movement
    enemyX += enemyX_change
    if enemyX < 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyY += enemyY_change
        enemyX_change = -4
# bullet movement
    if bullet_state is "fire":
        fire_bullets(playerX, bulletY)
        bulletY -= bulletY_change

    pygame.display.update()
