import random 

class Ball():
    def __init__(self, window_width, window_height):
        self.color = ((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.pos = [random.randint(0, window_width), random.randint(0, window_height)]
        self.speed = [random.uniform(2, 6), random.uniform(2, 6)]
        self.radius = random.randint(15,20)
        
    def move(self, window_width, window_height):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        if self.pos[0] <= 0 or self.pos[0] >= window_width:
            self.speed[0] = -self.speed[0]
        if self.pos[1] <= 0 or self.pos[1] >= window_height:
            self.speed[1] = -self.speed[1]
    
