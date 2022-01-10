class Surface_area():
    
    def circle_area(self,radius):
        self.radius=radius
        self.c_area=3.14*(self.radius*self.radius)
        print(f'{self.c_area}')
    def rectangle_area(self, side_1, side_2):
        self.side_1=side_1
        self.side_2=side_2
        self.r_area=self.side_1*self.side_2
        print(f'{self.r_area}')
    def triangle_area(self, base, height):
        self.base=base
        self.height=height
        self.t_area=(self.base*self.height)/2
        print(f'{self.t_area}')
a1=Surface_area()
a1.circle_area(3)
a2=Surface_area()
a2.rectangle_area(4,7)
a3=Surface_area()
a3.triangle_area(6,2)