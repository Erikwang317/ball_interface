import random 
import threading 
import time 

class Ball():
    def __init__(self, window_width, window_height):
        self.color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.pos = [random.randint(0, window_width), random.randint(0, window_height)]
        self.speed = [random.uniform(2, 6), random.uniform(2, 6)]
        self.radius = random.randint(15,20)
        self.lock = threading.Lock()
        
    def move(self, window_width, window_height):
        with self.lock:
            self.pos[0] += self.speed[0]
            self.pos[1] += self.speed[1]
            if self.pos[0] <= 0 or self.pos[0] >= window_width:
                self.speed[0] = -self.speed[0]
            if self.pos[1] <= 0 or self.pos[1] >= window_height:
                self.speed[1] = -self.speed[1]
                
    def manage(self, window_width, window_height, running_event):
        while running_event.is_set():
            self.move(window_width, window_height)
            time.sleep(0.016)
    
