import pygame
x = pygame.init()

# Creating window
gamewindow = pygame.display.set_mode((720,480))
pygame.display.set_caption("My First Game")

# Game Specific Variables
exit_game = False
game_over = False

# Creating the game loop
while not exit_game:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit_game = True

                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                                print("You have pressed right arrow key") 

                        if event.key == pygame.K_LEFT:
                                if event.key == pygame.K_LEFT:
                                        print("You pressed the left arrow key")     



pygame.quit
quit()