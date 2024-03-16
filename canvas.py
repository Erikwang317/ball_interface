import pygame
import random
import threading 
import time
from ball import Ball 

class Canvas(): 
    def __init__(self, ball_num=20, speed = [2,2], window_width=640, window_height=480):
        self.ball_num = min(50, ball_num)
        self.window_width = window_width
        self.window_height = window_height
        self.speed = speed
        self.balls = [Ball(window_width,window_height) for _ in range(self.ball_num)]  
        
    def draw_balls(self):
        for ball in self.balls:
            pygame.draw.circle(screen, ball.color, ball.pos, ball.radius)#self.ball_num)          


if __name__ == "__main__":
    pygame.init()
    canvas = Canvas()
    running_event = threading.Event()
    running_event.set()
    screen = pygame.display.set_mode((canvas.window_width, canvas.window_height))
    running = True
    showing_help = False
    clock = pygame.time.Clock()
    
    for ball in canvas.balls:
        thread = threading.Thread(target=ball.manage, args=(canvas.window_width, canvas.window_height, running_event))
        thread.start()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_a:
                    canvas.balls.append(Ball(canvas.window_width, canvas.window_height))
                    canvas.ball_num += 1
                if event.key == pygame.K_r and canvas.balls:
                    canvas.balls.pop()
                    canvas.ball_num -= 1
                if event.key == pygame.K_UP:
                    ball.speed[0] = ball.speed[0] * 1.1
                    ball.speed[1] = ball.speed[1] * 1.1
                if event.key == pygame.K_DOWN:
                    ball.speed[0] = ball.speed[0] * 0.9
                    ball.speed[1] = ball.speed[1] * 0.9
                    
        for ball in canvas.balls:
            ball.move(canvas.window_width, canvas.window_height)
                    
        screen.fill((0, 0, 0))
        canvas.draw_balls()
        pygame.display.flip()
        clock.tick(100)
        
    running_event.clear()
    pygame.quit()

