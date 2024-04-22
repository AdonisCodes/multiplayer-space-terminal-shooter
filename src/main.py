import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = pygame.Rect(300, 250, 50, 50)

run = True
while run:
    screen.fill([0, 0, 0])
    pygame.draw.rect(screen, (255, 0, 0), player)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        if player.x - 1 < 0:
            player.x = 0
        player.x -= 1
    if key[pygame.K_RIGHT]:
        if player.x + 1 > SCREEN_WIDTH - player.width:
            player.x = SCREEN_WIDTH - player.width
        player.x += 1
    if key[pygame.K_UP]:
        if player.y - 1 < 0:
            player.y = 0
        player.y -= 1
    if key[pygame.K_DOWN]:
        if player.y + 1 > SCREEN_HEIGHT - player.height:
            player.y = SCREEN_HEIGHT - player.height
        player.y += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
