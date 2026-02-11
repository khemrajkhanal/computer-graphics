import pygame
import sys 

pygame.init()
WIDTH , HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title="BLA Algortihm")

WHITE = (255,255,255)
BLACK = (0,0,0)

print("Enter x1 and y1")
x1 = int(input())
y1 = int(input())

print("Enter x2 and y2")
x2 = int(input())
y2 = int(input())

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

            # print(f"{x},{y}")

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        draw_line(x1,y1,x2,y2)

        pygame.display.flip()



if __name__ == "__main__":
    main()