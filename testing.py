import pygame
import random
import math
pygame.init()
screen_width = 1200
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
title=pygame.display.set_caption('FOR MY LOVE!!!!!')
pink = (255, 182, 193)
white = (255, 255, 255)
snowflake_color = (255, 255, 255)
clock = pygame.time.Clock()
font = pygame.font.Font(pygame.font.match_font('Comic Sans MS'), 60) 
fonts= pygame.font.Font(pygame.font.match_font('Ariel'),20)
start_time = pygame.time.get_ticks() / 1000.0

def draw_text(text,font,text_col,x,y):
    img=font.render(text,True,text_col)
    screen.blit(img, (x , y ))

def draw_heart(surface, color):
    heart_points = []
    for t in range(0, 361):
        t_rad = math.radians(t)
        x = 16 * (math.sin(t_rad) ** 3)
        y = 13 * math.cos(t_rad) - 5 * math.cos(2 * t_rad) - 2 * math.cos(3 * t_rad) - math.cos(4 * t_rad)
        heart_points.append((600 + x * 15, 300 - y * 15))

    pygame.draw.polygon(surface, color, heart_points)


class Snowflake:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = random.randint(-20, screen_height)
        self.size = random.randint(2, 5)
        self.speed = random.uniform(1, 3)
    def fall(self):
        self.y += self.speed
        if self.y > screen_height:
            self.y = -self.size
            self.x = random.randint(0, screen_width)
    def draw(self, screen):
        pygame.draw.circle(screen, snowflake_color, (int(self.x), int(self.y)), self.size)
snowflakes = [Snowflake() for _ in range(100)]


def main():
    running = True
    while running:
        screen.fill(pink)
        draw_heart(screen,(255,0,0))
        draw_text("I LOVE YOU SO MUCHHH!!!!",font,(white),200,250)
        draw_text("Made by Funez",fonts,(0,0,0),900,500)
        for snowflake in snowflakes:
            snowflake.fall()
            snowflake.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()
