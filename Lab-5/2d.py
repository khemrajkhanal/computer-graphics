import pygame
import sys 
import math

pygame.init()
WIDTH , HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title="2D Transformation")

WHITE = (255,255,255)
BLACK = (0,0,0)

print("Choose:")
print("1. Draw line")
print("2. Translation")
print("3. Scaling")
print("4. Reflection")
print("5. Rotation")
print("6. Exit")

user_choice = input("Enter your choice (1/2/3/4/5/6):")
if user_choice == '6':
    pygame.quit()
    sys.exit()
else: 
    print("Enter x1, y1:")
    x1 = int(input())
    y1 = int(input())
    print("Enter x2, y2:")
    x2 = int(input())
    y2 = int(input())

if user_choice == "2":
    print("Enter tx and ty :")
    tx = int(input())
    ty = int(input())
if user_choice == "3":
    print("Enter sx and sy :")
    sx = int(input())
    sy = int(input())
    print("Enter cx and cy:")
    cx = int(input())
    cy = int(input())
if user_choice == '4':
    axis = input("Enter axis:")
    print("Enter cx and cy:")
    cx = int(input())
    cy = int(input())
if user_choice == '5':
    # angle = int(input("Enter angle:"))
    print("Enter cx and cy:")
    cx = int(input())
    cy = int(input())
    
def draw_line(x1,y1,x2,y2):

    dx = abs(x2-x1)
    dy = abs(y2-y1) 

    if x2 > x1:
        lx = 1
    else:
        lx = -1

    if y2 > y1:
        ly = 1
    else:
        ly = -1

    x = x1
    y = y1

    if dx > dy:
        p = 2*dy - dx

        for i in range(dx + 1):
            screen.set_at((x,y),WHITE)
            x += lx
            if p < 0:
                y = y
                p = p + 2*dy
            
            else:
                y += ly
                p = p + 2*(dy - dx)

            # print(f"{x},{y}")

    else:
        p = 2*dx - dy

        for i in range(dy + 1):
            
            screen.set_at((x,y),WHITE)
            y += ly
            if p < 0:
                x = x
                p = p + 2*dx
            
            else:
                x += lx
                p = p + 2*(dx - dy)

def translate(x1,y1,x2,y2,tx,ty):
    x1_new = x1+tx
    y1_new = y1+ty
    x2_new = x2+tx
    y2_new = y2+ty
    
    draw_line(x1_new,y1_new,x2_new,y2_new)

def scaling(x1,y1,x2,y2,sx,sy,cx,cy):
    x1_new = int(cx + sx*(x1-cx))
    y1_new = int(cy + sy*(y1 - cy))
    x2_new = int(cx + sx*(x2-cx))               
    y2_new = int(cy + sy*(y2 - cy)) 
    draw_line(x1_new, y1_new, x2_new, y2_new)

def reflection(x1,y1,x2,y2,axis,cx,cy):
    def reflect_point(x,y):
        x = x - cx
        y = y - cy
        if axis == 'x':
            y = -y
        elif axis == 'y':
            x = -x
        return x +cx, y+cy
    x1_new, y1_new = reflect_point(x1, y1)
    x2_new, y2_new = reflect_point(x2, y2)
    draw_line(x1_new, y1_new, x2_new, y2_new)



def rotation(x1, y1, x2, y2, angle, cx, cy):
    rad = math.radians(angle)

    def rotate_point(x, y):
        x -= cx
        y -= cy

        x_new = x * math.cos(rad) - y * math.sin(rad)
        y_new = x * math.sin(rad) + y * math.cos(rad)

        return int(x_new + cx), int(y_new + cy)

    x1_new, y1_new = rotate_point(x1, y1)
    x2_new, y2_new = rotate_point(x2, y2)

    draw_line(x1_new, y1_new, x2_new, y2_new)




def main():
    angle = 0
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        draw_line(x1,y1,x2,y2)
        if user_choice == "2":
            translate(x1,y1,x2,y2,tx,ty)
        elif user_choice == "3":
            scaling(x1,y1,x2,y2,sx,sy,cx,cy)
        elif user_choice == "4":
            reflection(x1,y1,x2,y2,axis,cx,cy)
        elif user_choice == "5":
            rotation(x1, y1, x2, y2, angle, cx, cy)
                    
        angle+=1
        pygame.display.flip()



if __name__ == "__main__":
    main()