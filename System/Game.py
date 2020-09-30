
import pygame
import random
from enum import Enum

from definitions import Screen


class Direction(Enum):
    UP = 1,
    DOWN = 2,
    LEFT = 3,
    RIGHT = 4


class Game:

    def __init__(self):
        # Initialize pygame library
        pygame.init()
        # Initialize font module
        pygame.font.init()
        # Create the window
        self.__screen = pygame.display.set_mode((Screen.WIDTH, Screen.HEIGHT))
        # Set window caption
        pygame.display.set_caption(Screen.CAPTION)
        # Create red apple 10x10
        self.__apple = pygame.Surface((10, 10))
        self.__apple.fill((255, 0, 0))
        self.__applePos = (0, 0)
        # Create clock
        self.__clock = pygame.time.Clock()
        # Create the snake
        self.__snake = [(200, 200), (210, 200), (220, 200)]
        self.__snakeSprite = pygame.Surface((10, 10))
        self.__snakeSprite.fill((255, 255, 255))
        # Score
        self.__score = 0
        self.__font = pygame.font.SysFont("Courier New", 15)

    def __NewPos(self):
        """
        Get a random position in the screen in order to spawn the apple.
        """
        x = random.randint(0, Screen.WIDTH - 10)
        y = random.randint(0, Screen.HEIGHT - 10)
        return (x//10 * 10, y//10 * 10)

    def __Colision(self, obj1, obj2):
        return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])

    def Start(self):
        # Run until close the window
        running = True
        self.__applePos = self.__NewPos()
        direction = Direction.RIGHT
        while running:
            self.__clock.tick(10)   # 10 fps
            # The close button was clicked?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_UP) and (direction != Direction.DOWN):
                        direction = Direction.UP
                    if (event.key == pygame.K_DOWN) and (direction != Direction.UP):
                        direction = Direction.DOWN
                    if (event.key == pygame.K_LEFT) and (direction != Direction.RIGHT):
                        direction = Direction.LEFT
                    if (event.key == pygame.K_RIGHT) and (direction != Direction.LEFT):
                        direction = Direction.RIGHT

            # Add new element
            self.__snake = [self.__snake[0]] + self.__snake
            if direction == Direction.UP:
                self.__snake[0] = (self.__snake[0][0], self.__snake[0][1] - 10)
            elif direction == Direction.DOWN:
                self.__snake[0] = (self.__snake[0][0], self.__snake[0][1] + 10)
            elif direction == Direction.RIGHT:
                self.__snake[0] = (self.__snake[0][0] + 10, self.__snake[0][1])
            elif direction == Direction.LEFT:
                self.__snake[0] = (self.__snake[0][0] - 10, self.__snake[0][1])

            # Detect colision with apple
            if self.__Colision(self.__applePos, self.__snake[0]):
                self.__applePos = self.__NewPos()
                self.__score += 1
            else:
                # Remove last element of Snake
                self.__snake.pop()

            scoreStr = "Score: " + str(self.__score)
            scoreText = self.__font.render(scoreStr, False, (255, 255, 255))

            # Refresh screen
            self.__screen.fill((0, 0, 0))
            self.__screen.blit(self.__apple, self.__applePos)
            self.__screen.blit(scoreText, (5, 5))
            for pos in self.__snake:
                self.__screen.blit(self.__snakeSprite, pos)
            # Update the display
            pygame.display.update()
        # Quit window
        pygame.quit()
