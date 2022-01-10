class Arrays():

    @staticmethod
    def print_in_col(array):
        x=''
        for c in array:
           
            x=x+str(c)+","
        print(str(x[:-1]))
            
my_array = [4,1,8,7,2]
Arrays.print_in_col(my_array)