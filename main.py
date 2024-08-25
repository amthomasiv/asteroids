# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    #Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #updatable.add(player)
    #drawable.add(player)

    asteroid_grp = pygame.sprite.Group()
    Asteroid.containers = (asteroid_grp, updatable, drawable)

    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    
    while True:
        screen.fill((0,0,0))
        #player.update(dt)
        #player.draw(screen)

        for upd in updatable:
            upd.update(dt)

        for ast in asteroid_grp:
            if player.collision_check(ast):
                print("Game over!")
                sys.exit(0)
            
        for drw in drawable:
            drw.draw(screen)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
            
if __name__ == "__main__":
    main()



