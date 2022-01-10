class Phones():
    def __init__(self, name , memory, color):
        self.name=name
        self.memory=memory
        self.color=color
        self.is_on=False
        self.ph_ring=False
    def phone_on(self):
        self.is_on=True
    def phone_ring(self):
        self.ph_ring=True
    def phone_status(self):
        if (self.ph_ring)==False:
            print(f'Telefon:\nNazwa:{self.name}\nPamięć:{self.memory}\nKolor:{self.color}\n')
            if(self.is_on)==True:
                print(f'Telefon jest włączony')
            else:
                print(f'Telefon jest wyłączony')
        else:
            print(f'Telefon dzwoni! Odbierz!')
p1=Phones('Xiaomi',64,'pink')
p2=Phones('LG',64,'gold')
p1.phone_status()
p2.phone_status()
p1.phone_on()
p1.phone_status()
p2.phone_on()
p2.phone_ring()
p2.phone_status()


