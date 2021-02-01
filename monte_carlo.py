import pygame, random, sys
from dot import Dot
pygame.init()

pygame.display.set_caption('¡Monte Carlo!')

width,height = 500,500
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)

#height of the window is greater than heigh beacause variable height is used to make the circle and there needs to be room below the circle for the digits of pi
win = pygame.display.set_mode((width, height+50))

#takes in tke x and y of the dot (between -1, and 1) and return the coordinates where that dot should be drawn on the screen
def get_drawing_coords(d):

    draw_x = d.x * 250 + 250
    draw_y = d.y * -250 +250
    return (draw_x, draw_y)

#for adding text to the screen
def make_text(message, position, color = (0,0,0), font_size = 32):

    font = pygame.font.Font('freesansbold.ttf', font_size)
    text = font.render(str(message), True, color)
    text_rect = text.get_rect()
    text_rect.center = (position)
    return text, text_rect

#this function is called after every 100 dots to update the value of pi so that it doesn't change on the screen too fast
def pi_update(dots_in, total):
    return 4*dots_in/total


def game_loop():

    dots = []
    dots_in_cirlce = []
    pi = None

#draw the citcle in the center as well as the line of the bottom
    pygame.draw.circle(win, white, (width//2, height//2), width//2)
    pygame.draw.circle(win, black, (width//2, height//2), width//2-5)
    pygame.draw.rect(win, white, (0, height, width, 5))

    run = True
    while run:
        pygame.time.delay(5)

#check for user pressing x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #win.fill(black)

#create a new dot wit uniformly random coordinates
        new_dot = Dot(random.uniform(-1,1), random.uniform(-1,1))

#add the dot to the list of all dots and if it is in the circle add it to the list of the dots in the circle
        dots.append(new_dot)
        if new_dot.in_circle():
            dots_in_cirlce.append(new_dot)

#after 100 dots the value of pi is updated
        if len(dots) % 100 == 0:
            pi = pi_update(len(dots_in_cirlce), len(dots))

#checks what color the dot should be drawn
        color = lambda d: green if d.in_circle() else red

#cover the old vlaue of pi in black then draw the new one
        pi_text, pi_text_rect = make_text(str(pi), (width//2, height+ 30), (255,255,255))
        pygame.draw.rect(win, black, (0, height+5, width, 45))
        win.blit(pi_text, pi_text_rect)

#draw the dot
        pygame.draw.circle(win, color(new_dot), get_drawing_coords(new_dot), 1)

        pygame.display.flip()

game_loop()
