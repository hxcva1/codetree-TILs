word = ['L', 'E', 'B', 'R', 'O', 'S']

ch = input()

idx = -1

for i, c in enumerate(word):
    if (c == ch):
        idx = i
if idx == -1:
    print("None")
else:
    print(idx)