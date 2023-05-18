class Dog:
    # Class attribute
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    # Another instance method
    def speak(self, sound):
       return f"{self.name} says {sound}"

def obj_methods (obj) :
        return [method_name for method_name in dir(obj)
                if callable(getattr(obj, method_name))]
class JackRussellTerrier(Dog):
    pass
class Dachshund(Dog):
     def speak(self, sound = 'the end is near'):
        return f"{self.name} always says {sound}"
       
class Bulldog(Dog):
    
    def describe (self):
        return f"{self.name} has little hair"
dash = Dachshund('dash', 2)
bill  = Bulldog('bill', 4)
print('the end')

