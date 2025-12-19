import sys
import logger
import pygame
import player
import asteroid
import asteroidfield
import shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    dt, elapsedTime = 0, 0
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}\n")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()   
    shots = pygame.sprite.Group()

    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, drawable)

    asteroidFieldInstance = asteroidfield.AsteroidField()
    playerInstance = player.Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        logger.log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        elapsedTime = pygame.time.Clock().tick(60)
        dt = elapsedTime / 1000

        screen.fill("black")

        updatable.update(dt)
        asteroids.update(dt)
        shots.update(dt)

        for element in drawable:
            element.draw(screen)

        for asteroidElemnt in asteroids:
            if(asteroidElemnt.collides_with(playerInstance) == True):
                logger.log_event("player_hit")
                print(f"Game over!")
                sys.exit()
            
            for shotElemnt in shots:
                if (asteroidElemnt.collides_with(shotElemnt) == True):
                    logger.log_event("asteroid_shot")
                    shotElemnt.kill()
                    asteroidElemnt.split()
                    break

        pygame.display.flip()


if __name__ == "__main__":
    main()
