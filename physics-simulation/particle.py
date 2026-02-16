"""
Particle class (Handles ball physics and rendering)
"""

import pygame
import numpy as np
import random
from config import *

class Particle:
    def __init__(self, x, y, color=None, radius=None):
        self.position = np.array([x,y], dtype=float)
        self.velocity = np.array([0.0,0.0], dtype=float)
        if radius is None:
            self.radius = random.randint(8,25)
        else:
            self.radius = radius

        if color is None:
            self.color = random.choice(COLOR_LIST)
        else:
            self.color = color

        self.lifetime = 255
        self.fade_speed = random.uniform(0.5, 2.0)

    @property
    def mass(self):
        return self.radius ** 2 / 100

    def apply_forces(self, wind_force, mouse_force, gravity):
        # ball falling
        self.velocity[1] += gravity
        # wind force
        self.velocity += wind_force / self.mass
        # mouse force
        self.velocity += mouse_force / self.mass

    def update(self, wind_force = np.array([0.0, 0.0]), mouse_force=np.array([0.0, 0.0]), gravity=GRAVITY):
        self.apply_forces(wind_force, mouse_force, gravity)
        self.position += self.velocity
        self.check_collision()
        self.lifetime -= self.fade_speed

        if self.lifetime < 0:
            self.lifetime = 0

    def is_dead(self):
        return self.lifetime <= 0

    def check_collision(self):
        if self.position[1] + self.radius > HEIGHT:
            self.position[1] = HEIGHT - self.radius
            self.velocity[1] = -self.velocity[1] * BOUNCE_DAMPING

        if self.position[1] - self.radius < 0:
            self.position[1] = self.radius
            self.velocity[1] = -self.velocity[1] * BOUNCE_DAMPING

        if self.position[0] + self.radius > WIDTH:
            self.position[0] = WIDTH - self.radius
            self.velocity[0] = -self.velocity[0] * BOUNCE_DAMPING

        if self.position[0] - self.radius < 0:
            self.position[0] = self.radius
            self.velocity[0] = -self.velocity[0] * BOUNCE_DAMPING

    def draw(self, screen):
        pos = (int(self.position[0]), int(self.position[1]))

        # alpha = int(self.lifetime)
        # glow_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        #
        # glow_scale = self.radius / 20
        #
        # glow_radius_1 = int(self.radius + 15 * glow_scale)
        # glow_color_1 = (*self.color, 20)
        # pygame.draw.circle(glow_surface, glow_color_1, pos, glow_radius_1)
        #
        # glow_radius_2 = int(self.radius + 10 * glow_scale)
        # glow_color_2 = (*self.color, 40)
        # pygame.draw.circle(glow_surface, glow_color_2, pos, glow_radius_2)
        #
        # glow_radius_3 = int(self.radius + 5 * glow_scale)
        # glow_color_3 = (*self.color, 80)
        # pygame.draw.circle(glow_surface, glow_color_3, pos, glow_radius_3)
        #
        # screen.blit(glow_surface, (0, 0))
        # surf_size = self.radius * 3
        # center = (surf_size // 2, surf_size // 2)
        # particle_surface = pygame.Surface((surf_size, surf_size), pygame.SRCALPHA)
        # particle_color = (*self.color, alpha)
        # pygame.draw.circle(particle_surface, particle_color, center, self.radius)

        # screen.blit(particle_surface, (pos[0] - surf_size // 2, pos[1] - surf_size // 2))
        pygame.draw.circle(screen,self.color,pos,self.radius)