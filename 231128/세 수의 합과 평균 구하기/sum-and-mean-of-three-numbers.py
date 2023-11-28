a = input(). split()
a = list(map(int, a))

print(sum(a))
print(f"{sum(a) / len(a):.0f}")