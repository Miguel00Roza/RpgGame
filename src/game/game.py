import pygame

def RunGame():
    pygame.init()

    # Tamanho da tela
    screen = pygame.display.set_mode((800, 600))
    # Titulo
    pygame.display.set_caption("RPG Game")

    clock = pygame.time.Clock()

    player_sprite = pygame.image.load("./src/assets/teste.png").convert()

    player_sprite = pygame.transform.scale(player_sprite, (player_sprite.get_width() * 2, player_sprite.get_height() * 2))
    x = 100
    y = 100
    position = (100, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()

        

        screen.fill((30, 30, 30))
        position = (x, y)
        screen.blit(player_sprite, position)

        pygame.display.flip()
        clock.tick(30) # Limite de 30 fps
    
    pygame.quit()

RunGame()