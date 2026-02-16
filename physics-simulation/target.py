""" Target Class"""
import pygame
import random
import numpy as np

from config import *

class Target:
    def __init__(self):
        self.radius = random.choice([15, 25, 35])
        if self.radius == 15:
            self.score = SCORE_SMALL_TARGET
            self.color = TARGET_COLOR[0]
        elif self.radius == 25:
            self.score = SCORE_MEDIUM_TARGET
            self.color = TARGET_COLOR[1]
        else:
            self.score = SCORE_LARGE_TARGET
            self.color = TARGET_COLOR[2]

        side = random.choice(['top', 'bottom', 'left', 'right'])

        if side == 'top':
            self.position = np.array([random.randint(50, WIDTH -50), 0], dtype=float)
            self.velocity = np.array([random.uniform(-1, 1), TARGET_SPEED], dtype=float)
        elif side == 'bottom':
            self.position = np.array([random.randint(50, WIDTH - 50), HEIGHT], dtype=float)
            self.velocity = np.array([random.uniform(-1, 1), -TARGET_SPEED], dtype=float)
        elif side == 'left':
            self.position = np.array([0, random.randint(0, HEIGHT - 50)], dtype=float)
            self.velocity = np.array([TARGET_SPEED, random.uniform(-1, 1)], dtype=float)
        else:
            self.position = np.array([WIDTH, random.randint(50, HEIGHT - 50)], dtype=float)
            self.velocity = np.array([-TARGET_SPEED, random.uniform(-1, 1)], dtype=float)

        self.hit = False

    def update_target(self):
        self.position += self.velocity

    def is_off_screen(self):
        return (self.position[0] < -50 or self.position[0] > WIDTH + 50 or
                self.position[1] < -50 or self.position[1] > HEIGHT + 50)

    def check_hit(self, particle):
        distance = np.linalg.norm(particle.position - self.position)
        return distance < (self.radius + particle.radius)

    def draw(self, screen):
        pos = (int(self.position[0]), int(self.position[1]))
        if not self.hit:
            pygame.draw.circle(screen, WHITE, pos, self.radius, 3)
            pygame.draw.circle(screen, self.color, pos, self.radius - 5)
            pygame.draw.circle(screen, WHITE, pos, 5)

            font = pygame.font.Font(None, 20)
            score_text = font.render(str(self.score), True, WHITE)
            text_rect = score_text.get_rect(center=pos)
            screen.blit(score_text, text_rect)

