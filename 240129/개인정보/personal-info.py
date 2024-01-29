class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

persons = []

for _ in range(5):
    name, h, w = tuple(input().split())
    persons.append(Person(name, int(h), float(w)))

persons.sort(key=lambda x : x.name)
print("name")
for p in persons:
    print(p.name, p.h, p.w)
print()
print("height")
persons.sort(key=lambda x : -x.h)
for p in persons:
    print(p.name, p.h, p.w)