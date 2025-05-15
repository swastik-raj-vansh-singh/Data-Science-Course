# creating a virtual environment:

# dictionaries

students = {"name":['swastik','shruti'], "age" : [4,6]}
print (students['name'][1])

students['gender'] = ["M","F"]
print (students)

# looping through the dict
for key in students:
    print(key)

for value in students.values():
    print(value)

for key,value in students.items():
    print (f"{key} - {value}")

s = "my name is swastik"
words = s.split()
print(words)

# count the frequency of workd
dict = {}
for word in words :
    dict[word] = dict.get(word,0) +1

print (dict)