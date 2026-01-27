import pygame
import sys 
import math

pygame.init()
WIDTH , HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title="3D Transformation")

WHITE = (255,255,255)
BLACK = (0,0,0)

cube_vertices = [(-50,-50,-50),(-50,50,-50),(50,50,-50),(50,-50,-50)
                 ,(-50,-50,50),(-50,50,50),(50,50,50),(50,-50,50)]

cube_edge = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6)
             ,(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]

print("Choose:")
print("1. Original Cube")
print("2. Translation")
print("3. Rotation")
print("4. Scaling")
print("5. Reflection")
print("6. Exit")

user_choice = input("Enter your choice (1/2/3/4/5/6):")
if user_choice == '6':
    pygame.quit()
    sys.exit()

def translate(vertices, tx, ty, tz):
    result = []
    for x,y,z in vertices:
        result.append((x+tx,y+ty,z+tz))
    return result


def rotate(vertices, angle):
    result = []
    rad = math.radians(angle)
    for x,y,z in vertices:
        x_new = x*math.cos(rad) - z*math.sin(rad)
        z_new = x*math.sin(rad) - z*math.cos(rad)
        result.append((x_new,y,z_new))
    return result


def scaling(vertices, sx,sy,sz):
    result = []
    for x,y,z in vertices:
        result.append((sx*x,sy*y,sz*z))
    return result


def reflection(vertices, axis):
    result = []
    if axis == "x":
        for x,y,z in vertices:
            result.append((x,-y,-z))
    elif axis == "y":
        for x,y,z in vertices:
            result.append((-x,y,-z))
    elif axis == "z":
        for x,y,z in vertices:
            result.append((x,-y,-z))
    return result
                
                
def projection(points):
    x,y,z = points
    distance = 200
    scale = distance / (distance-z)
    screen_x = x + WIDTH//2
    screen_y = -y + WIDTH//2
    screen_x *= scale
    screen_y *= scale
    return (int(screen_x), int(screen_y))    


def draw_cube(vertices):
    projected = []
    for v in vertices:
        projected.append(projection(v))
    for edge in cube_edge:
        start = projected[edge[0]]
        end = projected[edge[1]]
        pygame.draw.line(screen, WHITE, start, end)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
        
        screen.fill(BLACK)
        original = cube_vertices
        translated = translate(cube_vertices,200,0,0)
        rotated = rotate(cube_vertices,20)
        scaled = scaling(cube_vertices, 10,10,10)
        reflected = reflection(cube_vertices,"x")
        
        if user_choice == '1':
            draw_cube(original)
        elif user_choice == '2':
            draw_cube(translated)
        elif user_choice == '3':
            draw_cube(rotated)
        elif user_choice == '4':
            draw_cube(scaled)
        elif user_choice == '5':
            draw_cube(reflected)
        

        pygame.display.flip()



if __name__ == "__main__":
    main()