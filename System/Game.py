
import pygame


class Game:

    def __init__(self, screen_width, screen_height, caption):
        # Initialize pygame library
        pygame.init()
        # Create the window
        self.__screen = pygame.display.set_mode((screen_width, screen_height))
        # Set window caption
        pygame.display.set_caption(caption)

    def start(self):
        # Run until close the window
        running = True
        while running:
            # The close button was clicked?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Draw a solid blue circle in the center
            pygame.draw.circle(self.__screen, (0, 0, 255), (250, 250), 75)
            # Flip the display
            pygame.display.flip()
        # Quit window
        pygame.quit()
