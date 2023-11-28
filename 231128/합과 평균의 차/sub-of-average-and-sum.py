a = input(). split()
a = list(map(int, a))

print(f"{sum(a)}\n{sum(a) // len(a)}\n{sum(a) - (sum(a) // len(a))}")