class Korean_BBQ:
    restaurant = "Charm_BBQ"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"
def obj_methods (obj) :
    return [method_name for method_name in dir(obj)
            if callable(getattr(obj, method_name))]
class JackRussellTerrier(Korean_BBQ):
    def speak(self, sound = 'bowwow'):
        return f"{self.restaurant} always says {sound}"
class Dachshund(Korean_BBQ):
    def speak(self, sound = 'bowwow'):
        return f"{self.restaurant} always says {sound}"
class Bulldog(Korean_BBQ):
    def describe (self):
        return f"{self.restaurant} has short hair"
dash = Dachshund('dash', 2)
bill = Bulldog('bill', 4)
print ('END')