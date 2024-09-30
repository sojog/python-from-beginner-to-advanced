
import enum

class ProgrammingLanguages(enum.Enum):
    Python = 1
    Java = 2
    CSharp = 3
    JavaScript = 4


lang1 = ProgrammingLanguages.Python
lang2 = ProgrammingLanguages.Java
lang3 = ProgrammingLanguages.CSharp

print(lang1 == lang2)
print(lang1 != lang2)

lang4 = ProgrammingLanguages(1)
print(lang4)