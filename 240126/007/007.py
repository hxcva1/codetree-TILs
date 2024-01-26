class Person:
    def __init__ (self, code, place, time):
        self.code = code
        self.place = place
        self.time = time
a = input().split()

person1 = Person(a[0], a[1], a[2])
print(f"secret code : {person1.code}")
print(f"meeting point : {person1.place}")
print(f"time : {person1.time}")