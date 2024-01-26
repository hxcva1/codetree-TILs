class Person:
    def __init__(self, id_ = "codetree", lv = 10):
        self.id_ = id_
        self.lv = lv
id_, lv = input().split() 
person1 = Person()
person2 = Person(id_,lv)
print(f"user {person1.id_} lv {person1.lv}")
print(f"user {person2.id_} lv {person2.lv}")