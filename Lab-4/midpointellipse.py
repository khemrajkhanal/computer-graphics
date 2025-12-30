import pygame
import sys 
import random

pygame.init()
WIDTH , HEIGHT = 800,800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(title="MidPoint Ellipse Algortihm")

WHITE = (255,255,255)
BLACK = (0,0,0)

print("Enter the center of ellipse(x,y):")
x_k = int(input())
y_k = int(input())
print("Enter the major and minor axes:")
r_x = int(input())
r_y = int(input())



def draw_ellipse(x_k,y_k,r_x,r_y):
    x = 0
    y = r_y
    
    dx = 2*(r_y**2)*x
    dy = 2*(r_x**2)*y
    
    # Initial decision parameter of region 1
    p_1 = float(r_y**2 - (r_x**2)*r_y + (1/4)*(r_x**2))
    
    
    # for region 1
    while 2*(r_y**2)*x<=2*(r_x**2)*y:
        # print(x,y)
        set_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        x += 1
        if p_1 < 0:
            y = y
            p_1 = p_1 + 2*(r_y**2)*x + r_y**2
        else:
            y -= 1
            p_1 = p_1 + 2*(r_y**2)*x - 2*(r_x**2)*y  + r_y**2      
        screen.set_at((x+x_k,y+y_k),WHITE)
        screen.set_at((x+x_k,-y+y_k),WHITE)
        screen.set_at((-x+x_k,y+y_k),WHITE)
        screen.set_at((-x+x_k,-y+y_k),WHITE)

    # for region 2    
    while y != 0:
        
        p_2 = float(r_y**2*(x+0.5)**2 + r_x**2*(y-1)**2 - r_x**2*r_y**2)
        y -= 1
        if p_2 > 0:
            x = x
            p_2 = p_2 - 2*r_x**2*y +r_x**2
        else:
            x+=1
            p_2 = p_2 + 2*r_y**2*x - 2*r_x**2*y +r_x**2
            
        screen.set_at((x+x_k,y+y_k),WHITE)
        screen.set_at((x+x_k,-y+y_k),WHITE)
        screen.set_at((-x+x_k,y+y_k),WHITE)
        screen.set_at((-x+x_k,-y+y_k),WHITE)
            
        
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
        
        screen.fill(BLACK)
        draw_ellipse(x_k,y_k,r_x,r_y)

        pygame.display.flip()



if __name__ == "__main__":
    main()   