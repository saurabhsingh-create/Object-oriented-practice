
#Restart the session
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass

item1 = 'Phone'
item_price = 100
item_quantity = 5
item_price_total = item_price * item_price

print(item_price_total)

print(type(item1))
print(type(item_price))

#class str  -- so 'phone' is an intance of class string.
#item1 is instantiated by class string.

#It would be nice if we can create a data type of our own, it can be used in future.
#Creating an instance or creating an object is the same thing.

#Creating a class

class Item:
    pass
    #in future we will write some code, but temporarily we use it as pass

#Creating an instance
item1 =  Item()
#Simimlar to 
rand_str = str("678")

#We are allowed to assign some attributed to the instances of the class
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5

#Each 1 of the attribute is assigned to 1 instance of the class

print(type(item1))
print(type(item1.name))
print(type(item1.price))

#item1 is of data type of item. It is class of Item.

#We have created attributes we can also create methods.

#Methods
random_str = 'Hello world'
print(random_str.upper())

#Similarly we need to figure out how we can design methods to run on our instances. This needs to be done inside the class

class Item:
    def calculate_total_price(self):
        pass
        #Python passes the object itself as the first argument, when you go ahead and call those methods
        #Python tries to pass 1 argument and we are not receiving any parameter. So we always need atleast 1 paramter which is object.
        #It is called as self. can be anything
        
item1 =  Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5        

item2 =  Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 5

#run with self inside method. It will pass the object item1 as argumnet and return nothing
item1.calculate_total_price()


class Item:
    def __init__(self):
        print('I am created')
    def calculate_total_price(self, x,y):
        return x*y
  
item1 =  Item()   
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5   
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 =  Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 5
print(item2.calculate_total_price(item2.price, item2.quantity))


#Now we have a constrcutor __init__ . It is method with unique name which has special features.
# It is called as magic method.

#Here we are creating instance of a class
item1.name = 'Phone'
item1.price = 100
#Python executes __init__ function automatically when you create an isntance of a class.
#It means that once class is declared and since an instance is created. It will call the actions that are inside __init__ method.
# Everytime an instance is created python will run the method __init__ .

#Now one of the problem here is we still hard code the attributes. SO we can benefit from __init__ method.
#FOr each instance we create it will go ahead and call __init__ method automatically.
#Python in the background passes itself as the first argument.
# But we can add more arguments in init and with instance we can assign the argument.
 

class Item:
    def __init__(self, name):
        print(f'I am created: {name}' )
    def calculate_total_price(self, x,y):
        return x*y

item1 =  Item('Laptop') 
#Self method will allow us assign the attribute from the init method. So that we do not have to go and assign the attribute individually.
# We can dynamically assign an attribute to an instance with the magic method which is called as __init__.

class Item:
    def __init__(self, name):
        print(f'I am created: {name}' )
        self.name = name
        #This will allow us to remove item1.name = 'Laptop'.
        # Individually assigning attributes from outside will be removed.
    def calculate_total_price(self, x,y):
        return x*y


item1 =  Item('Phone')
item1.price= 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))
print(item1.name)

item2 =  Item('Laptop')
item2.price = 1000
item2.quantity = 5
print(item2.name)
print(item2.calculate_total_price(item2.price, item2.quantity))

#Now we can assign the attributes dynamically

class Item:
    def __init__(self, name, price, quantity):
        print(f'I am created: {name}' )
        self.name = name
        self.price =  price
        self.quantity = quantity
        #This will allow us to remove item1.name = 'Laptop'. allos us to define it inside the constructor
        # Individually assigning attributes from outside will be removed.
    def calculate_total_price(self, x,y):
        return x*y

item1 =  Item('Phone', 100, 5)
item2 = Item('Laptop', 1000, 10)

print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate_total_price(item1.price, item1.quantity))

print(item2.name)
print(item2.price)
print(item2.quantity)
print(item2.calculate_total_price(item2.price, item2.quantity))

#Additional notes for working with classes.
#When we create __init__ method, this does not mean we cannot differentiate between mandatory or non mandtory paramters.
# We can bydefault receive a paramter as 0, if we do not know it. 

class Item:
    def __init__(self, name, price, quantity=0):
        print(f'I am created: {name}' )
        self.name = name
        self.price =  price
        self.quantity = quantity
        #This will allow us to remove item1.name = 'Laptop'. allos us to define it inside the constructor
        # Individually assigning attributes from outside will be removed.
    def calculate_total_price(self, x,y):
        return x*y
    
item1 =  Item('Phone', 100, 5)

print(item1.quantity)
print(item1.calculate_total_price(item1.quantity, item1.price)) 
#Here we have defined the quantity outside as 5, but it is not mandatory


item1 =  Item('Phone', 100)
print(item1.quantity)
print(item1.calculate_total_price(item1.quantity, item1.price)) 

#We can assign attributes to specific instances individually. Here instance is item1 and item2
#Eg - If a laptop has numpad or or not. But this question is not applicable for both phones and laptop, just for laptop.

item2 =  Item('Laptop', 1000)
print(item2.quantity)
print(item2.calculate_total_price(item2.quantity, item2.price)) 
item2.has_numpad = False
print(item1.has_numpad)

#for each method designed in the class. Object itself is passed as an argument. This is the problem we need to understand init and methods in class.
#So we directly use self.x * self.y to not pass argument.


class Item:
    def __init__(self, name, price, quantity=0):
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def calculate_total(self):
        return self.price * self.quantity
    
item3 = Item('Car', 10000, 5)
print(item3.quantity)
print(item3.price)
print(item3.name)
print(item3.calculate_total())

#If string used as inpput
item3 = Item('Car', '10000', 5)
print(item3.calculate_total())

#Sometimes we need an argumnet of fixed type. But we cannot have the condition of negative only or positive only numbers.
#But we can use assert statement
class Item:
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0
        assert quantity >= 0
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        #Run validation to recieve argumnets
        # assert price>=0
        # assert quantity>=0
    def calculate_total(self):
        return self.price * self.quantity

item3 = Item('Car', -10000, 5)         
#This will give assertion error.
print(item3.quantity)
print(item3.price)
print(item3.name)
print(item3.calculate_total())

#with exception
class Item:
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        #Run validation to recieve argumnets
        # assert price>=0
        # assert quantity>=0
    def calculate_total(self):
        return self.price * self.quantity

item3 = Item('Car', -10000, 5)         
#This will give assertion error.
print(item3.quantity)
print(item3.price)
print(item3.name)
print(item3.calculate_total())   

#Assert statement allows us to validate the argumnets and catch up the bugs.

#Global variables: class attributes that is shared across all the instances.
#This is specific to a class and it is available from all teh instances, while the instance levela ttributes are defined inside
#The  argumnets.

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        #Run validation to recieve argumnets
        # assert price>=0
        # assert quantity>=0
    def calculate_total(self):
        return self.price * self.quantity

item1 = Item('Car', 10000, 5) 
item2 = Item('Phone',100, 2)        
#to access the gloabl attribute
print(Item.pay_rate)
print(item1.pay_rate)
print(item2.pay_rate)

#The instance item1 and item2, that could not find pay_rate at instance level goes ahead and finds it in class level attributes.
#__dict__ is a magic attribute used to get the attributes belonging to a paticular object

print(Item.__dict__)
#This will list down all the attributes and functions of it. Class level attributes
print(item1.__dict__)
#This will print all the instance lebel attributes.

#Now use global variable in a method

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        #Run validation to recieve argumnets
        assert price>=0
        assert quantity>=0
    def calculate_total(self):
        return self.price * self.quantity
    
    def discount_price(self):
        return self.price * self.pay_rate
        
        
        #Here for the global variable we can access it using the object and not using self. keyword.
        #This will go ahead and over write the price attribute.
item1 = Item('Car', 10000, 5) 
print(Item.pay_rate)
print(item1.discount_price())
print(item1.price)

#Now if we want to have seperate discount for a particular product, we can define it seperatly.
item1 = Item('Car', 10000, 5) 
item1.pay_rate = 0.7
print(item1.discount_price())
print(item1.price)        
#So even thoughwe have defined our own attribute for the instance, it will return the same value.
#This is because the method of discount_price has a gloabl variable being multiplied.
#So the best way is to use self.pay_rate instead of Item.pay_rate
    

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price

    def calculate_total(self):
        return self.price * self.quantity
    
    def discount_price(self):
        self.price = self.price * self.pay_rate

item1 = Item('Car', 10000, 5) 
print(Item.pay_rate)
print(item1.discount_price())
print(item1.price)
        
item1 = Item('Car', 10000, 5) 
item1.pay_rate = 0.7
print(item1.discount_price())
print(item1.price)        


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)




class Item:
    all = []
    pay_rate =0.8
    def __init__(self, name: str, price:float, quantity =0):
        self.name = name
        self.price = price
        self.quantity = quantity
        assert price>=0, f"Price {price} should be greater than 0"
        assert quantity>=0, f"Price {price} should be greater than 0"
        Item.all.append(self)
    def calculate_total(self):
        return self.price * self.quantity
    def calclulate_discount(self):
        self.price= self.price * self.pay_rate        


item1 = Item("Phone", 100, 10)
item2 = Item("Phone", 100, 10)

item1.calclulate_discount()
item1.calculate_total()


#COnsider now you will have more items in the shop Item.
#It would have been nicer if we could have all the item instances that have been created until this point.
#We can do this using a work around as __init__ method is called everytime an instance is created.


class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        #Actions to execute
        Item.all.append(self)
    #So we created alist, using the init method which calls self or instance. We can add the instance name in it.
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def discount_price(self):
        self.price = self.price * self.pay_rate
#__repr__  -- used to get the argumnets passed.    
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity} )"


item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)
#Using the loop to print it
print(Item.all)
#This is the best practice and help us create instance immediately.
 
for i in Item.all:
    print(i.name, i.price)

#We can also pass the data inside a csv
import os
os.getcwd()
os.chdir(r'C:\Users\saurabhsingh\Downloads\Python programs')

import pandas as pd
pd.read_csv('input.csv')

#Now we can instantiate in more generic way.

################################## Class method #######################################

#We will have to crteate a method. But we cannot call it from in an instance.
#So we need to call the method of creating objects inside the class using some other way or converting it to class method.
# A class method is something that can be accessed like class attribute like -- Item.pay_rate
# It can be accessed from class level only, but to convert it we need a decorator.

import csv
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        
        #Actions to execute
        Item.all.append(self)
    #So we created alist, using the init method which calls self or instance. We can add the instance name in it.
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def discount_price(self):
        self.price = self.price * self.pay_rate
    
    #TO read from csv
    
        #in each method we need receive atleast 1 parameter that we have to pass.
        # We are not going to call the method from an instance.
        # We need to convert it to a class method.
        # Class method can only be accessd from class only.
# Class attribute is >>>> Item.pay_rate
# Class method >> Item.instantiate_from_csv()
        # we need to use a decorator to convert this method into a class method.
        # Decortators inpython are just used to chnage the behavior of the functions that we write.
    @classmethod   #Decorator
    def instantiate_from_csv(cls):
        # When we call a class method than the class object is passed as a argument always in the background.
        # write the code to read csv file and instantiate some objects.
        with open('input.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            print(item)
        
#__repr__  -- used to get the argumnets passed.    
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity} )"


Item.instantiate_from_csv()
print(Item.all)



#instantiate the class using the class method an print it.


import csv
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        
        #Actions to execute
        Item.all.append(self)
    #So we created alist, using the init method which calls self or instance. We can add the instance name in it.
    
    def calculate_total(self):
        return self.price * self.quantity
    
    def discount_price(self):
        self.price = self.price * self.pay_rate
    
    #TO read from csv
    
        #in each method we need receive atleast 1 parameter that we have to pass.
        # We are not going to call the method from an instance.
        # We need to convert it to a class method.
        # Class method can only be accessd from class only.
# Class attribute is >>>> Item.pay_rate
# Class method >> Item.instantiate_from_csv()
        # we need to use a decorator to convert this method into a class method.
        # Decortators inpython are just used to chnage the behavior of the functions that we write.
    @classmethod   #Decorator
    def instantiate_from_csv(cls):
        # When we call a class method than the class object is passed as a argument always in the background.
        # write the code to read csv file and instantiate some objects.
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
        return f"{self.__class__.__name__}Item('{self.name}',{self.price},{self.quantity} )"


Item.instantiate_from_csv()
print(Item.all)


# This was class method.
# Jump to static methdod


################################# Static Method #################################

# if you want to check if a number is int or float, we use static method.


import csv
class Item:
    pay_rate = 0.8 #The pay rate after 20% discount.
    all = []
    def __init__(self, name:str, price : float, quantity =0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        
        Item.all.append(self)
      
    def calculate_total(self):
        return self.price * self.quantity
    
    def discount_price(self):
        self.price = self.price * self.pay_rate
    

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
    
    #Static method
    #To check if a number is integer or not.
    #We will use a decorator to convert it to static method.
    @staticmethod
    def is_integer(num): #Static method is never sending instance as the 1st argument.
    #Class method will always run with __init__ but static wont.
    #It is like regular function.
        # TO get integer we will ignore float that are .0.
        if isinstance(num, float):
            return num.is_integer()  #is_integer method counts out the value that are .0.
        elif isinstance(num, int):
            return True
        else:
            return False
            
  
    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.quantity} )"

print(Item.is_integer(10.0))


### When to use class method, when to use a static method?
class Item:
    pass
#we will use static method, when we want to do something that is not unique to per instance.
#It is general and can be used with multiple instances of a class.
#We use class method majorly for insantiating class objects like from a csv or json or yaml files.
#If you are looking to instantiate 100 of objects, that is why we need atleats 1 class method.
# Main differnece is -- static method we dont pass object refernce as 1st argument.
#Static method and and class method can only be called from class level.

#But howver they can also be called fROM instance.
#In class method the argument passed thru is mandatory while in static method the parameter is optional.

item1 = Item('lap', 1000)
item1.is_integer(10.1)

#We generally dont call static method or class method from in instance.

## now we need to have seperate method for a instance.
#Lets say we want broken phones section for phone instance. We will need inheritance.
#The seperate class will inherit the functionalityof item class.

##################### Class inheritance #######################

class Phone(Item):#here we speicfy the class we will inherit from.
    pass

item1 = Phone('Oneplus', 1000, 3)
# Here we have inherited the  properties of item to Phone class.
#The classes from which we inherit is called as parent class and the properties inherited to is called
# as child class

#It is not great idea to assign attributes manually.
#create a constructor(init), and pass teh value in instance creation.


class Phone(Item):#add broken phones argumnet in inherited class.
    all = []
    def __init__(self, name:str, price : float, quantity =0, broken_phones = 0):
        #Run validation to recieve argumnets
        assert price >= 0, f"Price {price} is not greater than equal to 0"
        assert quantity >= 0,  f"Quantity {quantity} is not greater than equal to 0"
        assert broken_phones >=0, f"The number {broken_phones} should be positive"
        #Assign to self object
        self.name = name
        self.quantity = quantity
        self.price = price
        
        self.broken_phones = broken_phones
        
        Phone.all.append(self)
        
    def calculate_total(self):
        return self.price * self.quantity
    
phone1 = Phone('Oneplus', 1000, 10,2)        
print(phone1.calculate_total())

#Here class to init superclass is missed, we are calling consutuctor of child class.
#Using a super, will allow us to use parent class attributes, instead of defining it in child class.
#if we simply remove the lines and run the code it will give error.

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

# For each child class we use seperate constructor, we also need su[per function to get acceess of all attributes and method.

print(Item.all)
print(Phone.all)
#The super function will run the init function in the parent class.
#calling the class attribute from item class gives us more idea.
     
#self.__class__.__name__} this allows us to get class name.



# We need to start working with multiple files. Parent class and child class will be in different files.
# The main.py filr will only contain instances of parent class.

