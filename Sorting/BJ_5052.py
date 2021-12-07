t = int(input())  # 테스트 케이스 수 입력


def compare_num():
    for i in range(len(num_list)-1):
        if num_list[i] == num_list[i+1][0:len(num_list[i])]:
            # num_list 에서 두 개씩 전화번호를 비교, (0-1, 1-2, 2-3, ....)
            print('NO')
            return
    print('YES')


for _ in range(t):
    n = int(input())  # 전화번호 개수 입력
    num_list = []  # 전화번호 목록 저장 공간

    for i in range(n):
        # 전화번호 수만큼 번호를 입력받아, 공백을 제거해 저장
        num_list.append(input().strip())

    num_list.sort()
    compare_num()
