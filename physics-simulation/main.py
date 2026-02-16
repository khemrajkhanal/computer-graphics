# import pygame
import sys
import time
from target import *
# from config import *
# import numpy as np
from particle import *

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Physics Simulation")

clock = pygame.time.Clock()

particles = []

# if GAME_MODE:
score = 0
targets = []
game_start_time = time.time()
last_target_spawn = time.time()
game_over = False
game_won = False

def create_initial_particles():
    particles.clear()
    for i in range(5):
        x = WIDTH//2 + (i-2) * 50
        y = 100
        particles.append(Particle(x,y))

create_initial_particles()


font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None,24)

dragging = False
drag_start_pos = None
current_mouse_pos = None

paused = False

wind_force = np.array([0.0, 0.0])
mouse_gravity_active = False
mouse_repel_active = False
current_gravity = GRAVITY

def calculate_mouse_force(particle_pos, mouse_posi, strength):
    """ calculate attraction/repulsion force from mouse to particle and return force vector [fx,fy]"""
    direction = mouse_posi - particle_pos
    distance = np.linalg.norm(direction)
    if distance < 1:
        return np.array([0.0, 0.0])

    direction_normalized = direction / distance # normalized direction (length = 1 )
    force_magnitude = strength / (distance * 0.01)
    force = direction_normalized * force_magnitude

    return force

def resolve_particle_collision(res_particles):
    num_particles = len(res_particles)

    for i in range(num_particles):
        for j in range(i + 1, num_particles):
            particle_a = res_particles[i]
            particle_b = res_particles[j]

            direction = particle_b.position - particle_a.position
            distance = np.linalg.norm(direction)

            min_distance = particle_a.radius + particle_b.radius

            if min_distance > distance > 0:
                normal = direction / distance

                overlap = min_distance - distance
                separation = normal * (overlap / 2)

                particle_a.position -= separation
                particle_b.position += separation

                relative_velocity = particle_a.velocity - particle_b.velocity
                velocity_along_normal = np.dot(relative_velocity, normal)

                if velocity_along_normal > 0:
                    impulse = velocity_along_normal * COLLISION_DAMPING
                    impulse_vector = impulse * normal

                    particle_a.velocity -= impulse_vector
                    particle_b.velocity += impulse_vector



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # mouse_x,mouse_y = pygame.mouse.get_pos()
            # particles.append(Particle(mouse_x,mouse_y))
            dragging = True
            drag_start_pos = pygame.mouse.get_pos()

        if event.type ==pygame.MOUSEBUTTONUP:
            if dragging and drag_start_pos:
                drag_end_pos = pygame.mouse.get_pos()

                vx = (drag_end_pos[0] - drag_start_pos[0]) * VELOCITY_SCALE
                vy = (drag_end_pos[1] - drag_start_pos[1]) * VELOCITY_SCALE

                new_particle = Particle(drag_start_pos[0],drag_start_pos[1])
                new_particle.velocity = np.array([vx,vy], dtype=float)
                particles.append(new_particle)

            dragging = False
            drag_start_pos = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                particles.clear()

            if event.key == pygame.K_r:
                if GAME_MODE:
                    particles.clear()
                    targets.clear()
                    score = 0
                    game_start_time = time.time()
                    last_target_spawn = time.time()
                    game_over = False
                    game_won = False
                    print("Game restarted!")
                else:
                    create_initial_particles()

            if event.key == pygame.K_SPACE:
                paused = not paused

            if event.key == pygame.K_UP:
                current_gravity += GRAVITY_CHANGE
                print(f"Gravity: {current_gravity:.2f}")

            if event.key == pygame.K_DOWN:
                current_gravity -= GRAVITY_CHANGE
                print(f"Gravity: {current_gravity:.2f}")

    # Continuous key checking
    keys = pygame.key.get_pressed()
    wind_force = np.array([0.0, 0.0])
    if keys[pygame.K_LEFT]:
        wind_force[0] = -WIND_STRENGTH
    if keys[pygame.K_RIGHT]:
        wind_force[0] = WIND_STRENGTH

    mouse_gravity_active = keys[pygame.K_g]
    mouse_repel_active = keys[pygame.K_f]
    if dragging:
        current_mouse_pos = pygame.mouse.get_pos()

    trail_surface = pygame.Surface((WIDTH, HEIGHT))
    trail_surface.set_alpha(150)
    trail_surface.fill(BLACK)
    screen.blit(trail_surface, (0, 0))

    if not paused:

        if GAME_MODE and not game_over:
            elapsed_time = time.time() - game_start_time
            remaining_time = GAME_TIME_LIMIT - elapsed_time
            if remaining_time < 0:
                game_over = True
                game_won = score >= 500

            if time.time() - last_target_spawn > TARGET_SPAWN_INTERVAL:
                if len(targets) < MAX_TARGETS:
                    targets.append(Target())
                    last_target_spawn = time.time()

            for target in targets:
                target.update_target()

            targets[:] = [t for t in targets if not t.is_off_screen() and not t.hit]

        mouse_pos = np.array(pygame.mouse.get_pos(), dtype=float)

        for particle in particles:
            mouse_force = np.array([0.0, 0.0])

            if mouse_gravity_active:
                mouse_force = calculate_mouse_force(particle.position, mouse_pos, MOUSE_GRAVITY_STRENGTH)

            elif mouse_repel_active:
                mouse_force = -calculate_mouse_force(particle.position, mouse_pos, MOUSE_REPEL_STRENGTH)

            particle.update(wind_force, mouse_force, current_gravity)

        resolve_particle_collision(particles)

        particles[:] = [p for p in particles if not p.is_dead()]
        if GAME_MODE:
            for particle in particles:
                for target in targets:
                    if not target.hit and target.check_hit(particle):
                        target.hit = True
                        score += target.score
                        print(f"HIT! +{target.score} points. Total: {score}")


    for particle in particles:
        particle.draw(screen)

    if GAME_MODE:
        for target in targets:
            target.draw(screen)

    if dragging and drag_start_pos and current_mouse_pos:
        pygame.draw.line(screen, WHITE, drag_start_pos, current_mouse_pos, 2)
        pygame.draw.circle(screen, YELLOW, drag_start_pos, 5)

    if mouse_gravity_active or mouse_repel_active:
        mouse_pos = pygame.mouse.get_pos()
        color = GREEN if mouse_gravity_active else RED
        pygame.draw.circle(screen, color, mouse_pos, 30, 2)

    if GAME_MODE:
        score_text = font.render(f"Score: {score}", True, YELLOW)
        screen.blit(score_text, (10, 10))

        if not game_over:
            elapsed_time = time.time() - game_start_time
            remaining_time = max(0, GAME_TIME_LIMIT - elapsed_time)
            timer_color = RED if remaining_time < 10 else WHITE
            timer_text = font.render(f"Time: {int(remaining_time)}s", True, timer_color)
            screen.blit(timer_text, (WIDTH - 150, 10))
        target_text = small_font.render(f"Targets: {len(targets)}", True, WHITE)
        screen.blit(target_text, (10, 50))

        inst_lines = [
            "Drag to shoot particles at targets!",
            "G-Attract | F-Repel | L/R-Wind",
            "Hit targets before time runs out!",
            "Small=100pts | Medium=50pts | Large=25pts"
        ]
        y_pos = 80
        for line in inst_lines:
            text = small_font.render(line, True, WHITE)
            screen.blit(text, (10, y_pos))
            y_pos += 22

        if game_over:
            overlay = pygame.Surface((WIDTH, HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            screen.blit(overlay, (0, 0))

            if game_won:
                result_text = font.render("YOU WIN!", True, GREEN)
            else:
                result_text = font.render("GAME OVER", True, RED)

            result_rect = result_text.get_rect(center=(WIDTH //2, HEIGHT //2 - 50))
            screen.blit(result_text, result_rect)

            final_score = font.render(f"Final Score: {score}", True, WHITE)
            score_rect = final_score.get_rect(center=(WIDTH //2, HEIGHT //2))
            screen.blit(final_score, score_rect)

            restart_text = small_font.render("Press R to Restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT //2 + 50))
            screen.blit(restart_text, restart_rect)

    else:

        count_text = font.render(f"Particles: {len(particles)}", True, WHITE)
        screen.blit(count_text, (10,10))

        inst_lines = [
            "Drag mouse to throw particles",
            "C -> Clear | R -> Reset | SPACE -> Pause",
            "Hold G - Attract to mouse | Hold F - Repel from mouse",
            f"UP/DOWN - Adjust gravity (Current: {current_gravity:.2f})"
        ]
        y_pos = 50
        for line in inst_lines:
            text = small_font.render(line, True, WHITE)
            screen.blit(text, (10,y_pos))
            y_pos += 22

        if paused:
            pause_text = font.render("PAUSED", True, RED)
            text_rect = pause_text.get_rect(center=(WIDTH // 2, 30))
            screen.blit(pause_text, text_rect)

    y_indicator = HEIGHT - 60
    if wind_force[0] != 0:
        wind_text = small_font.render(f"Wind: {'->' if wind_force[0] > 0 else '<-'}", True, CYAN)
        screen.blit(wind_text, (10, y_indicator))

    if mouse_gravity_active:
        grav_text = small_font.render("ATTRACTING", True, GREEN)
        screen.blit(grav_text, (10, y_indicator + 20))

    elif mouse_repel_active:
        repel_text = small_font.render("REPELLING", True, RED)
        screen.blit(repel_text, (10, y_indicator + 20))



    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()