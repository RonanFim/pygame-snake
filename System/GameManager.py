
import pygame
import random
import time

from System.Direction import Direction
from System.Snake import Snake
from System.Apple import Apple
from System.Wall import Wall
from System.Score import Score
from definitions import GameProp


class GameManager:

    def __init__(self):
        # Create the window
        self.__screen = pygame.display.set_mode((GameProp.SCREENWIDTH, GameProp.SCREENHEIGHT))
        # Create elements
        self.__clock = pygame.time.Clock()
        self.__apple = Apple()
        self.__snake = Snake()
        self.__score = Score()
        self.__wall = Wall()

    def __NewPos(self):
        """
        Get a random position in the screen in order to spawn the apple.
        """
        while 42:
            x = random.randint(0, GameProp.SCREENWIDTH - 10)
            y = random.randint(0, GameProp.SCREENHEIGHT - 10)
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
        while running:
            self.__clock.tick(10)   # 10 fps
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
