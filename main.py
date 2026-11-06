import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, TARGET_FPS
from logger import log_state
from player import Player

def main() -> None:
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        dt = clock.tick(TARGET_FPS) / 1000 # convert from miliseconds to seconds by dividing by 1000


if __name__ == "__main__":
    main()
