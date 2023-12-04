m = int(input())

if m < 3 or m == 12:
    print("Winter")
elif m < 6:
    print("Spring")
elif m < 9:
    print("Summer")
else:
    print("Fall")