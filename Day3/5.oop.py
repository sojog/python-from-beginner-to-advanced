
class Animal:
    def __init__(self, name, weight, age = 0) -> None:
        # Public attributes
        self.name = name
        self.age = age
        # Internal attributes
        self._weight = weight 
        # Private attributes
        self.__hair_color = "red"

    def __str__(self) -> str:
        return f"{self.name} has {self.age} years"
    
    def change_hair_color(self, new_color):
        self.__hair_color = new_color

    ## getter
    @property
    def hair_color(self):
        return self.__hair_color

obj = Animal("Rino", 7)
print(obj)

print(obj._weight)
print(obj._Animal__hair_color)

# Name mangling
obj._Animal__hair_color = "blue blue blue"
print(obj._Animal__hair_color)

obj.change_hair_color("gray")
print(obj._Animal__hair_color)

print(obj.hair_color)

obj.hair_color = "black"

obj2 = Animal("Gira", 5, 2)
print(obj2)

obj3 = obj2
print(obj3)

obj_to_str = str(obj)
print("obj_to_str", obj_to_str)

