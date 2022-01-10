import random
x = round(random.uniform(34.0,42.0),1)
class Thermometer():
    def __init__(self):
        self.is_on=False
    def Thermometer_on(self):
        self.is_on=True
    def Thermometer_off(self):
        self.is_on=False
    def Temperature (self):
        self.temperature=x
    def Temperature_status(self):
        print(f'Temperatura:{self.temperature}C')
        if(self.temperature)>37 and (self.temperature)<41:
            print(f'Gorączka')
        elif(self.temperature)>41:
            print(f'Gorączka \nTEMPERATURA KRYTYCZNA!!') 