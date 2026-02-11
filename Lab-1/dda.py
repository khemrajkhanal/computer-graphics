import pygame
import sys 

pygame.init()
WIDTH , HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title="DDA Algortihm")

WHITE = (255,255,255)
BLACK = (0,0,0)

x1 = int(input("Enter first x cordinate:"))
y1 = int(input("Enter first y cordinate:"))

x2 = int(input("Enter final x cordinate:"))
y2 = int(input("Enter final y cordinate:"))


def calculate_points(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    
    steps = max(abs(dx), abs(dy))

    if dx>dy:
        steps = dx
    else:
        steps = dy

    x_inc = dx/steps
    y_inc = dy/steps

    x = x1
    y = y1
    screen.set_at((round(x), round(y)), WHITE)

    for i in range(steps+1):
        x= x+x_inc
        y = y+y_inc
        screen.set_at((round(x), round(y)), WHITE)


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(BLACK)
        calculate_points(x1,y1,x2,y2)
        
        pygame.display.flip()



if __name__ == "__main__":
    main()