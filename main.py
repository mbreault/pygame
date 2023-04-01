import pygame
import sys

def main():
    # Initialize the PyGame library.
    pygame.init()

    # Create a window.
    screen = pygame.display.set_mode((640, 480))

    # Draw a text label that says "hello, world!"
    text = pygame.font.SysFont("Arial", 24).render("hello, world!", True, (255, 0, 0))
    screen.blit(text, (200, 200))

    # Loop until the user closes the window.
    while True:
        # Check for events.
        for event in pygame.event.get():
            # If the user closed the window, exit the program.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update the screen.
        pygame.display.flip()

if __name__ == "__main__":
    main()