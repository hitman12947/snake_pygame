import pygame,random

pygame.init()

# Colors

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,50)

gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Saaaannnppppppp")
pygame.display.update()


def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow,color,snk_list,snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,210,229))
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():

    ## game varibles

    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 30
    init_velocity = 5
    velociy_x = 0
    velociy_y = 0
    food_x = random.randint(5,screen_width)
    food_y = random.randint(5,screen_height)
    snake_size = 10
    score = 0
    fps = 60

    snk_list = []
    snk_length = 1

    with open('highScore.txt', 'r') as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open('highScore.txt', 'w') as f:
                f.write(str(hiscore))
            gameWindow.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velociy_x = init_velocity
                        velociy_y = 0

                    if event.key == pygame.K_LEFT:
                        velociy_x = -init_velocity
                        velociy_y = 0

                    if event.key == pygame.K_UP:
                        velociy_x = 0
                        velociy_y = -init_velocity

                    if event.key == pygame.K_DOWN:
                        velociy_x = 0
                        velociy_y = init_velocity

            snake_x = snake_x + velociy_x
            snake_y = snake_y + velociy_y

            if abs(snake_x - food_x) < 6 and abs(snake_y-food_y) < 6:
                score += 10
                food_x = random.randint(20,screen_width / 2)
                food_y = random.randint(20,screen_height / 2)
                snk_length += 5

                if score > int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            text_screen("Score:" + str(score) +" HighScore "+ str(hiscore),red,5,5)
            pygame.draw.rect(gameWindow,red,[food_x,food_y,snake_size,snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over =True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
            # pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()