from item import Item

class Phone(Item):#add broken phones argumnet in inherited class.

    def __init__(self, name:str, price : float, quantity =0, broken_phones = 0):
        super().__init__(
            name, price, quantity 
            ##this is duplication and can be solved by keyword arguments.
            )
            
        
        self.broken_phones = broken_phones
        
        
    def calculate_total(self):
        return self.price * self.quantity
    
phone1 = Phone('Oneplus', 1000, 10,2)        
print(phone1.calculate_total())