""" This is the documentation for the module students """

class Student:
    """This is the documentation for the class Student from module students"""
    def __init__(self, name, age=18):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}"
    

def learn():
    """We explain how things go around here"""
    pass 
    
if __name__ == "__main__":
    std1 = Student("Ion")
    print(std1)
