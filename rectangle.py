class Rectangle: 
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h
        self.x = 0
        self.y = 0
        pass

    def get_coords(self):
        return self.x , self.y
    
    def get_dimensions(self):
        return self.width , self.height
    
    def move_up(self):
        if self.y > 0:
            self.y -= 1
    def move_down(self):
        if self.y < 19 - self.height + 1:
            self.y += 1
    def move_left(self):
        if self.x < 0:
            self.x -= 1
    def move_right(self): 
        if self.x < 19 - self.width + 1:
            self.x += 1
