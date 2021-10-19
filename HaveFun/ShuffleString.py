import random

# 원하는 문자열 입력
s = input()

# 문자열을 리스트로 저장할 공간
str_arr = []

# 빈칸 제거
s= ''.join(s.split())
print(s)

# 입력 문자열을 리스트에 추가
for i in s:
    str_arr.append(i)

# 리스트 랜덤 재배열
random.shuffle(str_arr)

# 셔플값 출력
for i in range(len(s)):
    print(str_arr[i], end='')
