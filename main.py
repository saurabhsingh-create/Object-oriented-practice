# We will use main.py file to only initiate instances.

from item import Item
from phone import Phone

Item.instantiate_from_csv()

print(Item.all)

item1 = Item("MyItem", 750)
#item1.name = "OtherItem"
#changing an attribute.

# We can also fix a value of a argumnet and we will have errors ehen we try to assign it.
# it is called as encapsulation

print(item1.read_only_name)

item1.read_only_name = "BBB"  #this will give error as it is readonly attribute.

#Biggest challenge is to convert the name attribite as read only.
# Once we put an arugumnet in @property, we cannot change it.
# using self._name in property constructor as well as init constructor can solve things

print(item1.name)
item1.name = 'Hello rld'
#item1.name = "OtherItem"  -- this will give error.

#Howeverr _name is still visible at instance level., to avoid it we use __name
#we want to prevent the access from item.
# __ this is called as private attribute and prevent the acceess totally outside of the class.
#changing the the _name to __name will also remove it from being visible from class instance.

#How to set a new value to such attributes used with property constructor.
#We would like to set a new value for the attribute.

# @name.setter --> we would still want to set a value for a attribute.
# It will allows us to set up a value and also to chnage it.
print(item1.name)
item1.name = 'Hello world'

#if the name is too long it will raise an exception. 
# we can set special beahviour to different attributes. We can delete some attributes from
# constructor and we can assign it using child class.



#name setter will always include additional parameter used to assign a value.
#getter wil go to the read only property, while setter will go to the name setter decorator.

#restricting the length of the correctors can also be done this needs to be done in setter.


############################ OOPS has 4 keys principle #########
# Encapsulation, abstraction, inheritance, polymorphism.


#1. Encapsulation:: restricting the direct access to some of the attributes.
# Restricting the ability to overwrite the values for your objects witin your setter is an example of encapsulation.

#We can have a method to incremnet this price and discount.

from item import Item
from phone import Phone

item1 = Item("MyItem", 750)
item1.price = 200  # we cannot set the attribute, as we have set it in property decorator/
print(item1.price)

item1.apply_increment(0.2)
# Soe venm thouugh we have capsulated/made attributes read only, we can still increment



#2. Abstraction : shows only necessary attributes and hides uncessary attributes to users.
# sending an email ha smultiple processes involved. we can alll combine int one method.
#All the methods will be visible, so we should hide those information.
# So we apply abstraction methods.
# We can create by adding __ to those methods. def __connect(self)
# So now we cannott access from instances as well.

# 3. Inheritance::
    # It allows us to use property to inherit items and methods.
phone1 = Phone('Oneplus', 1000, 10,2)        
print(phone1.calculate_total())
# Sowe can use entire class as it as well as modify existing method by inherting.


# 4. Polymorphism
# using single identity to represnt different types in different scenarios.
# refers to many forms. ability to have different sceanrios.

name = "Hello world"
len(name)
li = [1,2,"Jello"]
print(len(li))
#single entity is working differently.
#similarly we can use apply discount from phone as well as item class.
#inhertiance and polymorphism is called together at many places.
#single entity is being used from different objects.




