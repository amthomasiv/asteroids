import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, width=2)

    def move(self, dt):
        self.position += self.velocity * dt

    def update(self, dt):
        self.move(dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        rand_deg = random.uniform(20, 50)
        #a_velocity = self.velocity.rotate(rand_deg)
        #b_velocity = self.velocity.rotate(rand_deg * -1)

        chunk_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.position.x, self.position.y, chunk_radius)
        asteroid_b = Asteroid(self.position.x, self.position.y, chunk_radius)
        asteroid_a.velocity = self.velocity.rotate(rand_deg) * 1.2
        asteroid_b.velocity = self.velocity.rotate(rand_deg * -1) * 1.2
