import pygame
import sys 

pygame.init()
WIDTH , HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title="MidPoint Circle Algortihm")

WHITE = (255,255,255)
BLACK = (0,0,0)

print("Enter the radius:")
r = int(input())

x = 0
y = r
print("Enter the center of the circle:")
x1 = int(input())
y1 = int(input())
def draw_circle(x,y,r):
    


    # initial decision parameter
    d = 1-r

    while x<=y:
        screen.set_at((x+x1,y+y1),WHITE)
        screen.set_at((x+x1,-y+y1),"blue")
        screen.set_at((-x+x1,y+y1),"green")
        screen.set_at((-x+x1,-y+y1),"red")
        screen.set_at((y+y1,x+x1),"pink")
        screen.set_at((y+y1,-x+x1),"yellow")
        screen.set_at((-y+y1,x+x1),"orange")
        screen.set_at((-y+y1,-x+x1),"purple")

        x += 1
        if d < 0:
            y = y
            d = d + 2*x + 1
        else:
            y = y - 1
            d = d + 2*(x - y) + 1
        
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
        
        screen.fill(BLACK)
        draw_circle(x,y,r)

        pygame.display.flip()



if __name__ == "__main__":
    main()   