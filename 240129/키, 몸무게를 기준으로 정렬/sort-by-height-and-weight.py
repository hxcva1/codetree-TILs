class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

persons = []
n = int(input())
for _ in range(n):
    name, h, w = tuple(input().split())
    persons.append(Person(name, int(h), int(w)))

persons.sort(key=lambda x : (x.h, -x.w))
for p in persons:
    print(p.name, p.h, p.w)