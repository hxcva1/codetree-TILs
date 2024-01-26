n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

persons = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    persons.append(Person(name, height,weight))

persons.sort(key=lambda x : x.height)

for i in range(n):
    print(persons[i].name, persons[i].height, persons[i].weight)