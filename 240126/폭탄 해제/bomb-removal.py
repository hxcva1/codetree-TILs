class Mission:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second
code, color, second = tuple(input().split())
m = Mission(code, color, second)
print(f"code : {m.code}")
print(f"color : {m.color}")
print(f"second : {m.second}")