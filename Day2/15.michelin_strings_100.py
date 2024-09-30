
# %%
# Exercise 1
text1 = "Hello"
text2 = "World"
print(text1 + text2)

# %%
# Exercise 2
text = " all right "
print(text * 3)

# %%
# Exercise 3
text = "10" + "0" * 3
print(text)

# %%
# Exercise 4
text =  "3.1415"
number = 3.1415
print(text == number)

# %%
# Exercise 5
text1 =  "not all strings are create equal"
text2 =  '''not all strings are create equal'''
print(text1 == text2)

# %%
# Exercise 6
text1 =  """strings are awesome"""
text2 =  "strings are awesorne"
print(text1 != text2)

# %%
# Exercise 7
text1 =  """awesome"""
text2 =  "awesome"
print(text1 is text2)

# %%
# Exercise 8
text = "hello"
print("L" in text)

# %%
# Exercise 9
text = "Python is great."
print("python" not in text)

# %%
# Exercise 10
adjective = "Awesome"
print(not adjective)

# %%
# Exercise 11
text = 'good' or 'bad'
print(text)

# %%
# Exercise 12
text = 'good' and 'bad'
print(text)

# %%
# Exercise 13
text = 'Houston, we have a problem.'
print(len(text))

# %%
# Exercise 14
text = "caiac"
print(list(text))

# %%
# Exercise 15
text = "caiac"
print(set(text))

# %%
# Exercise 16
city1 = "Barcelona"
city2 = "Berlin"
print(city1 < city2)

# %%
# Exercise 17
text = "python"
print(text[2])

# %%
# Exercise 18
text = "python"
print(text[-2:])

# %%
# Exercise 19
word = "python"
print(word[::-1])

# %%
# Exercise 20
text = '{} {} {}'.format("Take", "Ianke", "Cadîr")
print(text)

# %%
# Exercise 21
movie = "The Godfather"
character = "Don Vito Corleone"
quote = "I'm gonna make him an offer he can't refuse."
print(f"In the movie '{movie}', {character} says: '{quote}'")

# %%
# Exercise 22
nr = 123111456
print(f"{nr:,}")

# %%
# Exercise 23
text = '1_111'
print(int(text))

# %%
# Exercise 24
text = "python programming"
print(text.title())

# %%
# Exercise 25
text = "python"
print(text.istitle())

# %%
# Exercise 26
text = "I love Python"
print(text.capitalize())

# %%
# Exercise 27
text =  "It's ALIVE!  It's ALIVE!"
print(text.swapcase())

# %%
# Exercise 27
text = "Python is powerful."
print(text.endswith("."))

# %%
# Exercise 28
name = "John Doe"
print(name.startswith("John"))

# %%
# Exercise 29
word = "banana"
print(word.count("a"))

# %%
# Exercise 30
text = "the good, the bad, the ugly"
print(text.find("the"))

# %%
# Exercise 31
text = 'My name is Bond, James Bond'
print(text.rfind("Bond"))

# %%
# Exercise 32
text = "the good, the bad, the ugly"
print(text.index("the"))

# %%
# Exercise 33
text = "Python is powerful."
print(text.partition("is"))

# %%
# Exercise 34
text = "Python is powerful."
print(text.rpartition("is"))

# %%
# Exercise 35
text = "Hasta la vista, baby."
print(text.replace("baby", "honey"))

# %%
# Exercise 36
text = "   Hit the road, Jack   "
print(text.strip())

# %%
# Exercise 37
text = "   What a wonderful world.   "
print(text.rstrip())

# %%
# Exercise 38
sentence = "May the Force be with you"
print(sentence.split())

# %%
# Exercise 39
email = "user@example.com"
print(email.split("@")[1])

# %%
# Exercise 40
phrase = "  Spaces around  "
print(len(phrase.strip().split()))

# %%
# Exercise 41
text = "Hello, how are you?"
print([len(word) for word in text.split()])

# %%
# Exercise 42
text = "123"
new_text = '1'.join(text)
print(new_text)

# %%
# Exercise 43
sentence = "This is a sentence."
print('-'.join(sentence.split()))

# %%
# Exercise 44
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(" I believe I can fly\n".join(days))

# %%
# Exercise 45
text = "Python is fun"
print(" ".join(text.split()[::-1]))

# %%
# Exercise 46
text = """Monday
    Tuesday
    Wednesday
    Thursday
    Friday
    Saturday
    Sunday
    learn
    Python"""
print(text.splitlines())

# %%
# Exercise 47
text = "python"
print(text[2::2])

# %%
# Exercise 48
text = "Imagination is more important than knowledge"
print(text.removeprefix("Imagination"))

# %%
# Exercise 49
text = "Be the change that you wish to see in the world."
print(text.removesuffix("int the world."))

# %%
# Exercise 50
text = "abc123"
print(text.isalnum())

# %%
# Exercise 51
text = "abc123"
print( text.isalpha())

# %%
# Exercise 52
text = "123 "
print( text.isnumeric())

# %%
# Exercise 53
text = "10o0"
print(text.isdecimal())

# %%
# Exercise 54
text = " 12345 "
print(text.isdigit())

# %%
# Exercise 55
text = "python"
print(text.isspace())

# %%
# Exercise 56
text = 'I\'m king of \the world!'
print(text)

# %%
# Exercise 57
# %%text =  "My 
#1 favorite is you? \n"
print(text.isprintable())

# %%
# Exercise 58
text = "Hello\tWorld!"
print(text.expandtabs(4))

# %%
# Exercise 59
text = "python"
print(text.isupper())

# %%
# Exercise 60
text = "Python is easy to learn."
print(text.upper().lower())

# %%
# Exercise 61
text = "hello"
print(text.rjust(10, '-'))

# %%
# Exercise 62
text = "Python programming is fun!"
print(text.center(30, '_'))

# %%
# Exercise 63
text = "python"
print(text.ljust(10, '*'))

# %%
# Exercise 64
number = "42"
print(number.zfill(5))

# %%
# Exercise 65
text = "Is it safe?"
print(text.replace("fun", "safe"))

# %%
# Exercise 66
text = "110101011"
print(int(text, 2))

# %%
# Exercise 67
text = "ABCDEF"
print(int(text, 16))

# %%
# Exercise 68
text = "Python"
print(list(enumerate(text)))

# %%
# Exercise 69
text = "Python"
print(''.join(char * 2 for char in text))

# %%
# Exercise 70
text = "Python programming is fun!"
print(text.split()[-1])

# %%
# Exercise 71
text = "May the Force be with you."
print(text[:10])

# %%
# Exercise 72
text = "You talking to me?"
print(text[:11]  if len(text) > 11 else text)

# %%
# Exercise 73
text = "May the Force be with you."
print(" ".join(text.split()[:3]))

# %%
# Exercise 74
text = "!emosewa si nohtyP"
print(text[::-1])

# %%
# Exercise 75
text = "I'm gonna make him an offer he can't refuse."
print(' '.join(word[::-1] for word in text.split()))

# %%
# Exercise 76
text = "Why don't scientists trust atoms? Because they make up everything!"
print(' '.join(reversed(text.split())))

# %%
# Exercise 77
days = "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
print(", ".join(sorted(days.split(", "))))

# %%
# Exercise 78
text = "Python is awesome"
reply = "Yes, it is" if text.isalpha() else "no, it is"
print(reply)

# %%
# Exercise 79
text = "Python is easy; python is powerful; python is versatile."
print(text.lower().split().count("Python".lower()))

# %%
# Exercise 80
text = "Oh-oh-oh-oh-oh, oh-oh-oh-oh, oh-oh-oh / Caught in a bad romance..."
print(any(char.istitle() for char in text))

# %%
# Exercise 81
text = "Python"
print(any(char.isdigit() for char in text))

# %%
# Exercise 82
text = "area 51"
print("".join(word for word in text if word.isalpha()))

# %%
# Exercise 83
text = "😀🌟📚🍕🌈🐱‍👤"
print(any(char.isalnum() for char in text))

# %%
# Exercise 84
text = "Let s loose them 🐱‍👤"
print( all(char.isalpha() or char.isdigit() for char in text))

# %%
# Exercise 85
text = "Python https://www.python.org/ is powerful."
print(any([word.startswith("http") and "." in word for word in text.split()]))

# %%
# Exercise 86
text = "Python is easy."
print(sum(1 for char in text if char.lower() in "aeiou"))

# %%
# Exercise 87
text = "to be or not to be that is the question"
print(" ".join([word.title() for word in text.split()]))

# %%
# Exercise 88
text = "to be or not to be that is the question"
print({word: text.split().count(word) for word in set(text.split())})

# %%
# Exercise 89
text = "the cat chased the dog"
print(text.replace("cat", "***").replace("dog", "cat").replace("***", "dog"))

# %%
# Exercise 90
text = "user@example.com"
print(text.split("@")[1].split(".")[0])

# %%
# Exercise 91
text = "Hello, how are you?"
print("".join(char for index, char in enumerate(text) if char not in text[:index]))

# %%
# Exercise 92
email = "user@domain.com"
print(all(['@' in email, '.' in email, email.split('@', 1)[0], email.split('@', 1)[1],  '.' in email.split('@', 1)[1], email.split('.', 1)[1]]))

# %%
# Exercise 93
text = "Welcome to the world of Python"
print(max(text.split(), key=len))

# %%
# Exercise 94
text = "Welcome to the world of Python"
print(list(sorted(text.split(), key=len)))

# %%
# Exercise 95
text = "12345"
print(any(char.isnumeric() or char.isalpha() for char in text))

# %%
# Exercise 96
text = "Python is easy."
print(sum(1 for char in text if char.isalpha() and char.lower() not in "aeiou"))

# %%
# Exercise 97
text = "x = 1, y = 5, z = 7"
print(''.join(str(int(char) + 10) if char.isdigit() else char for char in text))

# %%
# Exercise 98
text = "Hello, let's create a secret code using Python!"
emoji_mapping = str.maketrans({'a': 'v', 'e': '😎', 'o': '🥳', 'l': '🤓'})
print(text.translate(emoji_mapping))

# %%
# Exercise 99
text = "Python ™ is amazing!"
print(any(not char.isascii() for char in text))

# %%
# Exercise 100
text = "LikeTheVideoShareTheVideoSubscribeToTheChannel"
print(''.join(['_' + i.lower() if i.isupper() else i for i in text]).lstrip('_'))

# %%
# Exercise 101
import re

re.findall(r"Chuck", "There is no Esc key on Chuck Norris' keyboard, because no one escapes Chuck Norris. ")

# %%
# Exercise 102
import re

result = re.compile("Chuck")
result.findall("There is no Esc key on Chuck Norris' keyboard, because no one escapes Chuck Norris. ")

# %%
# Exercise 102
import re

re.split(r"\?", "Chuck Norris invented the internet? just so he had a place to store his porn.")

# %%
# Exercise 103
import re

re.split(r",", "If Chuck Norris writes code with bugs, the bugs fix themselves.")


# %%
# Exercise 104
import re

re.split(r"\?", "Chuck Norris invented the internet? just so he had a place to store his porn.")

# %%
# Exercise 105
re.sub(r"Oracle", "nice", "Chuck Norris doesn't use Oracle, he is the Oracle.")

# %%
# Exercise 106
import re

re.search(r"tests", "Don't worry about tests, Chuck Norris's test cases cover your code too.")

# %%
# Exercise 107
import re

print(re.match(r"tests", "Don't worry about tests, Chuck Norris's test cases cover your code too."))

# %%
# Exercise 108
import re

re.match(r"Don't", "Don't worry about tests, Chuck Norris's test cases cover your code too.")

# %%
# Exercise 109

xmasRegex = re.compile(r'\d+\s\w+')
list(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# %%
# Exercise 110
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('Chuck Norris breaks RSA 128-bit encrypted codes in milliseconds.')

# %%
# Exercise 111
vowelRegex = re.compile(r'[^aeiouAEIOU]')
print(vowelRegex.findall('Chuck Norris breaks RSA 128-bit encrypted codes in milliseconds.'))

# %% [markdown]
# ## Capturing Groups
# %%
# Exercise 112
import re

text = "Chuck Norris can delete the Recycling Bin."
# re.findall('[A-Za-z]', text) 

# %%
# Exercise 113
import re
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowelRegex.findall('RoboCop eats baby food. BABY FOOD.') 


# %%
# Exercise 114
import re

text = 'Clary has 2 friends who she spends a lot of time with. Susan has 3 brothers while John has 4 sisters.'
#re.findall('([A-Za-z]+)\s\w+\s\d+\s\w+', text)
re.findall('([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', text)

# %%
# Exercise 115
mo = re.search(r"(\d[A-Za-z])+", "My user name is 3e4r5fg")
print(mo)
print(type(mo))

# %%
# Exercise 116
mo.group()

# %%
# Exercise 117
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
'415'
print(mo.group(2))
'555-4242'
print(mo.group(0))
'415-555-4242' 
print(mo.group())
'415-555-4242'
mo.groups()
('415', '555-4242')
areaCode, mainNumber = mo.groups()
print(areaCode)
415
print(mainNumber)


