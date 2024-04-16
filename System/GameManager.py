
import pygame
import random
import time

from System.Direction import Direction
from System.Snake import Snake
from System.Apple import Apple
from System.Wall import Wall
from System.Score import Score
from System.Configuration import Configuration
from definitions import GameProp


class GameManager:

    def __init__(self, configs: Configuration):
        self.__configs = configs
        # Create the window
        self.__screen = pygame.display.set_mode((configs.width.value, configs.height.value))
        # Create elements
        self.__clock = pygame.time.Clock()
        self.__apple = Apple()
        self.__snake = Snake(configs)
        self.__score = Score()
        self.__wall = Wall(configs)

    def __NewPos(self):
        """
        Get a random position in the screen in order to spawn the apple.
        """
        while 42:
            x = random.randint(0, self.__configs.width.value - 10)
            y = random.randint(0, self.__configs.height.value - 10)
            newPos = (x//10 * 10, y//10 * 10)
            if not self.__wall.IsColliding([newPos]) and not self.__snake.IsColliding([newPos]):
                return newPos

    def __RefreshScreen(self):
        self.__screen.fill(GameProp.BGCOLOR)
        self.__score.Draw(self.__screen)
        self.__apple.Draw(self.__screen)
        self.__snake.Draw(self.__screen)
        self.__wall.Draw(self.__screen)

    def Start(self):
        # Run until close the window
        running = True
        paused = False
        self.__apple.SetApplePos(self.__NewPos())
        direction = Direction.RIGHT
        counter = 0
        while running:
            self.__clock.tick(GameProp.FPS)   # fps
            counter += 1
            if paused:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        # Resume game? (SPACE key)
                        if event.key == pygame.K_SPACE:
                            paused = not paused
                continue
            for event in pygame.event.get():
                # The close button was clicked?
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # Pause game? (SPACE key)
                    if event.key == pygame.K_SPACE:
                        paused = not paused
                    elif (event.key == pygame.K_UP):
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

            # Set speed
            if not(counter % self.__configs.speed.value):
                # Add new element
                self.__snake.Grow(direction)

                # Detect colision with apple
                if self.__snake.IsColliding([self.__apple.GetApplePos()]):
                    self.__apple.SetApplePos(self.__NewPos())
                    self.__score.IncrementScore()
                else:
                    # Remove last element of Snake
                    self.__snake.RemoveLast()

                # Detect colision with snake
                if self.__snake.SelfCollision():
                    time.sleep(2)
                    running = False
                # Detect colision with wall
                if self.__snake.IsColliding(self.__wall.GetWall()):
                    time.sleep(2)
                    running = False

            # Update the display
            self.__RefreshScreen()
            pygame.display.update()
    
        return self.__score.GetScore()
