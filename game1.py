import pygame

pygame.init()

#game window

pygame.display.set_mode((1200,300))
pygame.display.set_caption("My first game")

#game specific variables

exit_game = False
game_over = False

#creating game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            # if event.key:                                 // detact pressed key
            #     print(pygame.key.name(event.key))
            if event.key ==  pygame.K_RIGHT:
                print("Right key Pressed")




pygame.quit()
quit()