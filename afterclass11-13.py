import random
class Arrays():
    
    def addnum(self, number,value):
        self.number=number
        self.value=value
        list=[]
        for i in range(self.number+1):
            list.append(self.value)
        print(f'{list}')  
    def arrbt(self,number_of_array_elements, value_from, value_to):
        self.number_of_array_elements=number_of_array_elements
        self.value_fr=value_from
        self.value_t=value_to
        array=''
        for i in range(self.number_of_array_elements+1):
            array+=str(random.randint(self.value_fr,self.value_t))+','
        print(f'[{array[:-1]}]')
    

ar1=Arrays()
ar1.addnum(10,4)
ar2=Arrays()
ar2.arrbt(20,-7,8)

    
    
    