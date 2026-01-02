import pygame
 
def RunGame():
    pygame.init()

    # Tamanho da tela
    screen = pygame.display.set_mode((800, 600))
    # Titulo
    pygame.display.set_caption("RPG Game")

    clock = pygame.time.Clock()

    MAP = [
    "######################################",
    "######...............................#",
    "######B.......................FFFFFF.#",
    "######.............................F.#",
    "####..........................F....F.#",
    "#.............................FFFFFF.#",
    "#....................................#",
    "#...........T...................WWWWW#",
    "#..........T....................WWLWW#",
    "#..........T.........................#",
    "#.......TTTT.........................#",
    "#TTTTTTT.............FF.FFWWWWWWWWWWW#",
    "#.P..................F...FWWWWWWWWWWW#",
    "#....................FFFFFWWWWWWWWWWW#",
    "######################################"
    ]

    TILE = 32 # 32x32 pixels
    rocks = []
    walls = []
    grounds = []
    fences = []
    trees = []
    shop = []
    boss = []

    px = 0
    py = 0
    player_pos = (px, py)

    rock_color = (128,128,128)
    wall_color = (255,255,255)
    ground_color = (144,238,144)
    fence_color = (160,82,45)
    tree_color = (0,128,0)
    shop_color = (0,0,0)
    boss_color = (255,0,0)

    for y, line in enumerate(MAP):
        for x, col in enumerate(line):
            # coluna = letra, ou seja cada letra é uma coluna

            world_x = x * TILE
            world_y = y * TILE

            if col == "#":
                rocks.append(pygame.Rect(world_x, world_y, TILE, TILE))

            if col == "W":
                walls.append(pygame.Rect(world_x, world_y, TILE, TILE))
            
            if col == "F":
                fences.append(pygame.Rect(world_x, world_y, TILE, TILE))
            
            if col == "T":
                trees.append(pygame.Rect(world_x, world_y, TILE, TILE))
            
            if col == ".":
                grounds.append(pygame.Rect(world_x, world_y, TILE, TILE))
            
            if col == "B":
                boss.append(pygame.Rect(world_x, world_y, TILE, TILE))
            
            if col == "L":
                shop.append(pygame.Rect(world_x, world_y, TILE, TILE))
            
                
            if col == "P":
                px = world_x
                py = world_y

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
        
        pressed = pygame.key.get_pressed()
     
        # 2 - Atualiza a logica
        if pressed[pygame.K_UP]: py -= 3
        if pressed[pygame.K_DOWN]: py += 3
        if pressed[pygame.K_LEFT]: px -= 3
        if pressed[pygame.K_RIGHT]: px += 3


        # 3 - Desenha o mapa
        for wall in walls:
            pygame.draw.rect(screen, wall_color, wall)
        
        for ground in grounds:
            pygame.draw.rect(screen, ground_color, ground)
        
        for rock in rocks:
            pygame.draw.rect(screen, rock_color, rock)
        
        for bos in boss:
            pygame.draw.rect(screen, boss_color, bos)
        
        for sho in shop:
            pygame.draw.rect(screen, shop_color, sho)
        
        for fence in fences:
            pygame.draw.rect(screen, fence_color, fence)

        for tree in trees:
            pygame.draw.rect(screen, tree_color, tree)

        screen.blit(player, (px, py))
        pygame.display.flip()
        clock.tick(30) # Limite de 30 fps
    
    pygame.quit()

RunGame()