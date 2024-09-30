import students

obj1 = students.Student("Maria")
print(obj1)

# print(students)
# print(students.__name__)

# print(dir(obj1))

# print(dir(students))

# print(students.Student.__doc__)

# print(students.learn.__doc__)

print(dir(obj1))

obj1.on_the_fly = "yeee"
print(dir(obj1))

print(hasattr(obj1, "on_the_fly"))
print(hasattr(obj1, "not_here"))

print(type(obj1))
print(isinstance(obj1, students.Student))
print(isinstance(obj1, int))
print(type(obj1) == students.Student)