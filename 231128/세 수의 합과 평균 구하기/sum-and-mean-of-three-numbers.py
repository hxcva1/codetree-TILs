a = input(). split()
a = list(map(int, a))

print(sum(a))
print(f"{int(sum(a) / len(a))}")