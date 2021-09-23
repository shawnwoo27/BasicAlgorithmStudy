s = input()
zero = 0
one = 0

for i in range(0, len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            zero += 1
        else:
            one += 1

if s[len(s)-1] == '0':
    zero += 1
else:
    one += 1

a = [zero, one]
a.sort()

print(a[0])
