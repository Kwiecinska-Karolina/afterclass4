class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        if self.x>self.y:
            self.distance=self.x-self.y
        else:
            self.distance=self.y-self.x
    def __str__(self):
        if self.x != self.y:
            print(f'Odległość między punktami wynosi {self.distance}')
        else:
            print(f'Odległość między punktami wynosi 0')
    
p1=Point(20,8)
p1.__str__()
