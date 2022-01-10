class TV():
    def __init__(self):
        self.volume_value=0
    def add_1(self):
        self.volume_value+=1
    def sub_1(self):
        self.volume_value-=1
    def show_status(self):
        if(self.volume_value)>=0 and (self.volume_value)<=10:
            print(f'TV volume is {self.volume_value}')
        elif(self.volume_value)<0:
            print(f'TV volume is 0')
        else:
            print(f'TV volume is 10')
            
tv=TV()
tv.show_status()
tv.add_1()
tv.show_status()
tv.sub_1()
tv.show_status()

