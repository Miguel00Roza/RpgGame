import pygame
 
def RunGame():
    pygame.init()

    # Tamanho da tela
    screen = pygame.display.set_mode((800, 600))
    # Titulo
    pygame.display.set_caption("RPG Game")

    clock = pygame.time.Clock()

    MAP = [
    "####################",
    "#..................#",
    "#..................#",
    "#..................#",
    "#..P...............#",
    "#..................#",
    "####################"
    ]

    TILE = 32 # 32x32 pixels
    walls = []
    player_pos = None

    for y, line in enumerate(MAP):
        for x, col in enumerate(line):
            # coluna = letra, ou seja cada letra é uma coluna

            world_x = x * TILE
            world_y = y * TILE

            if col == "#":
                walls.append(pygame.Rect(world_x, world_y, TILE, TILE))

            if col == "P":
                player_pos = (world_x, world_y)

    player = pygame.image.load("./src/assets/teste.png").convert()
    
    running = True
    # Dentro do mapa inserimos apenas 3 coisas nesta ordem
    # 1 - Le inputs do player ( Teclado e mouse )
    # 2 - Atualiza a logica, ( Movimento, colisao, vida e etc... )
    # 3 - Desenha o mapa
    while running:
        # Lê inuts

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2 - Atualiza a logica



        # 3 - Desenha o mapa
        for wall in walls:
            pygame.draw.rect(screen, (100, 0, 100), wall)

        screen.blit(player, player_pos)
        pygame.display.flip()
        clock.tick(30) # Limite de 30 fps
    
    pygame.quit()

RunGame()