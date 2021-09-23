s = input()
result = 0

for i in range(0, len(s)):
    num = int(s[i])
    if num > 1:
        result *= num
    else:
        result += num

print(result)
