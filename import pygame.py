import pygame
import random

# Constants
WIDTH = 800
HEIGHT = 600
PARTICLE_COUNT = 100
PARTICLE_RADIUS = 5
MAX_PARTICLE_SPEED = 1
MAX_RANDOM_FORCE = 0.5

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-MAX_PARTICLE_SPEED, MAX_PARTICLE_SPEED)
        self.vy = random.uniform(-MAX_PARTICLE_SPEED, MAX_PARTICLE_SPEED)

    def move(self):
        random_force_x = random.uniform(-MAX_RANDOM_FORCE, MAX_RANDOM_FORCE)
        random_force_y = random.uniform(-MAX_RANDOM_FORCE, MAX_RANDOM_FORCE)

        self.vx += random_force_x
        self.vy += random_force_y

        # Update particle position
        self.x += self.vx
        self.y += self.vy

        # Boundary behavior: Bounce off edges
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brownian Motion Simulation")
clock = pygame.time.Clock()

# Create particles
particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(PARTICLE_COUNT)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update particles
    for particle in particles:
        particle.move()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw particles
    for particle in particles:
        pygame.draw.circle(screen, (255, 255, 255), (int(particle.x), int(particle.y)), PARTICLE_RADIUS)

    # Update the display
    pygame.display.flip()

    # Limit frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
