from logger import log_state
import pygame
import player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    dt, elapsedTime = 0, 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\n")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()

    playerInstance = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        elapsedTime = pygame.time.Clock().tick(60)
        dt = elapsedTime / 1000
        #print(f"DeltaTime: {dt}")

        screen.fill("black")
        playerInstance.update(dt)
        playerInstance.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
