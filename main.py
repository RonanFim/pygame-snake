
import pygame

def main():
    print("Hello")

    # Initialize pygame library
    pygame.init()

    # Set up the drawing window
    screen = pygame.display.set_mode((600, 600))
    # Set window caption
    pygame.display.set_caption('Snake')

    # Run until close the window
    running = True
    while running:
        # The close button was clicked?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
        # Flip the display
        pygame.display.flip()

    # Quit program
    pygame.quit()
    return 0


if __name__ == '__main__':
    main()
