class Student():
    
    def __init__(self,name,surname,field_of_study):
        self.name = name
        self.surname=surname
        ID=100000
        self.ID=ID+1
        self.field_of_study=field_of_study

    def __str__(self):
        print(f'{self.name} {self.surname} ({self.ID}), {self.field_of_study}, UEK Kraków ')
        
s1=Student('Anna','Maj', 'Informatyka Stosowana')
s2=Student('Adam','Nowak', 'Informatyka Stosowana')
s3=Student('Marcin','Kowal', 'Informatyka Stosowana')
s1.__str__()
s2.__str__()
s3.__str__()