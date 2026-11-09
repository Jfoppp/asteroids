import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TARGET_FPS
from logger import log_state, log_event
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main() -> None:
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    score = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game Over!")
                print(f"Score: {score}")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
                    score += 1
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(TARGET_FPS) / 1000 # convert from miliseconds to seconds by dividing by 1000


if __name__ == "__main__":
    main()
