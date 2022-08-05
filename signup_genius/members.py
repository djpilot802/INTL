import pandas as pd 
import numpy as np 

class member:
    def __init__(self, first, last, id, sober_date): 
        self.first = first
        self.last = last 
        self.id = id 
        self.sober_date = sober_date

    def fullname(self): 
        return '{}'' ''{}'.format(self.first,self.last)


mem_1 = member('Jac', 'Cottam', 1, '10/21/2022')
mem_2 = member('Bill', 'Collins', 2, '10/23/1995')

# Directly below shows a little bit more about how the functionality actually works since you're passing in the argument

print(member.fullname(mem_1))

# or you can use the below - which is easier to read 

print(mem_2.fullname())