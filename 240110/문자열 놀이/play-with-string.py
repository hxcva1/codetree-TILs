s, q = input().split()
s = list(s)
q = int(q)

for _ in range(q):
    n, a, b = input().split()
    if n == '1':
        a = int(a)
        b = int(b)
        s = list(s)
        temp = s[a-1]
        s[a-1] = s[b-1]
        s[b-1] = temp
        s = ''.join(s)
        print(s)
    else:
        s = list(s)
        for i in range(len(s)):
            if s[i] == a:
                s[i] = b
        s = ''.join(s)
        print(s)