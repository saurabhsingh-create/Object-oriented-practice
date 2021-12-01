
import csv
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self._name = name
        self.quantity = quantity
        self.__price = price
        
        #Actions to execute
        Item.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @property
    def price(self):
        return self.__price
    
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
    
    @name.setter 
    def name(self,value):
        if len(value)>10:
            raise Exception('The name is too long')
        else:
            self.__name = value

    # This will allow us to change the value.
    
    def calculate_total(self):
        return self.__price * self.quantity
    
    def discount_price(self):
        self.__price = self.__price * self.pay_rate
    
    
    @classmethod   #Decorator
    def instantiate_from_csv(cls):
    
        with open('input.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)
            Item(name = item.get('name'),
                 price = float(item.get('price')),
                 quantity = int(item.get('quantity')),  #price can be in decimals
                 )
        
#__repr__  -- used to get the argumnets passed.    
    def __repr__(self):
        return f"{self.__class__.__name__}Item('{self.name}',{self.__price},{self.quantity} )"
    
    @property
    def read_only_name(self):
        return "AAA"
        
    def __connect(self):
        pass
    
    def __email_body(self):
        return f"hello {self.name}"
    
    def __send(self):
        pass
    
    ## final method which will contain all methods
    def send_email(self):
        self.__read_only_name()
        self.__connect()
        self.__send()
    
    #
    