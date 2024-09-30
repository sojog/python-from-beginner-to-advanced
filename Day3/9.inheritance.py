from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, weight, age) -> None:
        self.weight = weight
        self.age = age
        self.__no_of_legs = 0

    def __str__(self):
        return f"W:{self.weight} A:{self.age}"
    
    @property
    def legs(self):
        return self.__no_of_legs
    
    @legs.setter
    def legs(self, new_value):
        self.__no_of_legs = new_value

    @abstractmethod
    def height(self):
        pass

class Cat(Animal):
    MAX_AGE = 35
    def __init__(self, name, weight, age) -> None:
        self.name = name
        super().__init__(weight, age)

    def __str__(self):
        return f"N: {self.name} {super().__str__() }" 
    
    # Overwriting the initial method
    def height(self):
        return 20
    
    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self.weight == other.weight and self.age == other.age
    
class BreedCat(Cat):
    def __init__(self, name, breed, weight, age) -> None:
        self.breed = breed
        super().__init__(name, weight, age)
    
    def __str__(self):
        return f"B: {self.breed} {super().__str__() }" 

if __name__ == "__main__":
    # animal1 = Animal(5, 1)
    
    cat = Cat("Rino", 5, 10)
    cat3 = Cat("Rino", 5, 10)
    cat4 = cat
    print(dir(cat))
    print(cat.legs)
    cat.legs = 4
    print(cat.legs)
    cat2 = Cat("Mao", 10, 6)
    rb = BreedCat("Theo", "Russian Blue", 5, 2)
    print(rb)

    print("Static AGE:", Cat.MAX_AGE)
    print("Static AGE from the object:", cat.MAX_AGE)

    Cat.MAX_AGE = 40
    print("Static AGE:", Cat.MAX_AGE)
    print("Static AGE from the object:", cat.MAX_AGE)

    cat.MAX_AGE = 50 
    print("Static AGE:", Cat.MAX_AGE)
    print("Static AGE from the object:", cat.MAX_AGE)
    print("Static AGE from the sencond object:", cat2.MAX_AGE)

    print(cat == cat2)
    print(cat == cat3)
    print(cat == cat4)
    