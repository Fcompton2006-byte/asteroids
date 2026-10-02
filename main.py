import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from logger import log_state
from asteroids import Asteroid
from asteroidsfield import AsteroidField
from logger import log_event
from shot import Shot
from score import Score
import sys

# Game
def main():

    # Start up print
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initiate game's base line 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)
    
    dt = 0.0

    # Establish groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    score = pygame.sprite.Group()

    # Establish containers tat devide up into groups
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)
    Score.containers = (score, updatable)

    # Establish the moving parts
    score = Score()
    player = Player(SCREEN_WIDTH/ 2, SCREEN_HEIGHT / 2)
    AsteroidField()
    while True:
        log_state()
        score_board = font.render(score.printout(), True, (255, 255, 255))

        # Make the exit work
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score.printout()
                return
        
        # Update everything that can be updated
        updatable.update(dt)

        # Make the astroids kill the player
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                return score.end_of_game()
                sys.exit()

        # Make the shots break astroids
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    score.hit(asteroid)
                    asteroid.split()
                    
        # Print the game to the screen
        screen.fill("black")
        screen.blit(score_board, (900, 100))
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
