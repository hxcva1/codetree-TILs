s = input()

for i in range(len(s)):
    if s[i].isalpha():
        print(s[i].upper(), end='')