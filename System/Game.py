
import pygame
import random
import time
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
        self.__snake = [(220, 200), (210, 200), (200, 200)]
        self.__snakeSprite = pygame.Surface((10, 10))
        self.__snakeSprite.fill((0, 153, 0))
        self.__headSprite = pygame.Surface((10, 10))
        self.__headSprite.fill((255, 255, 255))
        # Score
        self.__score = 0
        self.__font = pygame.font.SysFont("Courier New", 15)
        self.__scorePos = (20, 20)
        # Create wall
        self.__wall = []
        for i in range(0, Screen.HEIGHT, 10):
            self.__wall.append((i, 0))
            self.__wall.append((i, Screen.WIDTH - 10))
        for i in range(0, Screen.WIDTH, 10):
            self.__wall.append((0, i))
            self.__wall.append((Screen.HEIGHT - 10, i))
        self.__OpenWall()
        self.__wallSprite = pygame.Surface((10, 10))
        self.__wallSprite.fill((51, 25, 0))

    def __OpenWall(self):
        self.__wall.remove((0, 270))
        self.__wall.remove((0, 280))
        self.__wall.remove((0, 290))
        self.__wall.remove((0, 300))
        self.__wall.remove((0, 310))
        self.__wall.remove((0, 320))
        self.__wall.remove((0, 330))
        self.__wall.remove((590, 270))
        self.__wall.remove((590, 280))
        self.__wall.remove((590, 290))
        self.__wall.remove((590, 300))
        self.__wall.remove((590, 310))
        self.__wall.remove((590, 320))
        self.__wall.remove((590, 330))
        self.__wall.remove((270, 0))
        self.__wall.remove((280, 0))
        self.__wall.remove((290, 0))
        self.__wall.remove((300, 0))
        self.__wall.remove((310, 0))
        self.__wall.remove((320, 0))
        self.__wall.remove((330, 0))
        self.__wall.remove((270, 590))
        self.__wall.remove((280, 590))
        self.__wall.remove((290, 590))
        self.__wall.remove((300, 590))
        self.__wall.remove((310, 590))
        self.__wall.remove((320, 590))
        self.__wall.remove((330, 590))

    def __NewPos(self):
        """
        Get a random position in the screen in order to spawn the apple.
        """
        while 42:
            x = random.randint(0, Screen.WIDTH - 10)
            y = random.randint(0, Screen.HEIGHT - 10)
            newPos = (x//10 * 10, y//10 * 10)
            if (newPos not in self.__wall) and (newPos not in self.__snake):
                return newPos

    def __Colision(self, obj1, obj2):
        return (obj1[0] == obj2[0]) and (obj1[1] == obj2[1])

    def __RefreshPos(self, pos, direction):
        if direction == Direction.UP:
            newPos = [pos[0], pos[1] - 10]
            if newPos[1] < 0:
                newPos[1] = Screen.HEIGHT - 10
        elif direction == Direction.DOWN:
            newPos = [pos[0], pos[1] + 10]
            if newPos[1] >= Screen.HEIGHT:
                newPos[1] = 0
        elif direction == Direction.RIGHT:
            newPos = [pos[0] + 10, pos[1]]
            if newPos[0] >= Screen.WIDTH:
                newPos[0] = 0
        elif direction == Direction.LEFT:
            newPos = [pos[0] - 10, pos[1]]
            if newPos[0] < 0:
                newPos[0] = Screen.WIDTH - 10
        else:
            return pos
        # Modified position
        return tuple(newPos)

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
                    if (event.key == pygame.K_UP):
                        if (direction != Direction.DOWN):
                            direction = Direction.UP
                        break
                    elif (event.key == pygame.K_DOWN):
                        if (direction != Direction.UP):
                            direction = Direction.DOWN
                        break
                    elif (event.key == pygame.K_LEFT):
                        if (direction != Direction.RIGHT):
                            direction = Direction.LEFT
                        break
                    elif (event.key == pygame.K_RIGHT):
                        if (direction != Direction.LEFT):
                            direction = Direction.RIGHT

            # Add new element
            self.__snake = [self.__snake[0]] + self.__snake
            self.__snake[0] = self.__RefreshPos(self.__snake[0], direction)

            # Detect colision with apple
            if self.__Colision(self.__applePos, self.__snake[0]):
                self.__applePos = self.__NewPos()
                self.__score += 1
            else:
                # Remove last element of Snake
                self.__snake.pop()

            # Detect colision with snake
            if self.__snake[0] in self.__snake[1:]:
                time.sleep(3)
                running = False
            # Detect colision with wall
            if self.__snake[0] in self.__wall:
                time.sleep(3)
                running = False

            scoreStr = "Score: " + str(self.__score)
            scoreText = self.__font.render(scoreStr, False, (255, 255, 255))

            # Refresh screen
            self.__screen.fill((0, 0, 0))
            self.__screen.blit(self.__apple, self.__applePos)
            self.__screen.blit(scoreText, self.__scorePos)
            self.__screen.blit(self.__headSprite, self.__snake[0])
            for pos in self.__snake[1:]:
                self.__screen.blit(self.__snakeSprite, pos)
            for pos in self.__wall:
                self.__screen.blit(self.__wallSprite, pos)
            # Update the display
            pygame.display.update()
        # Quit window
        pygame.quit()
