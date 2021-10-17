# 올바른 괄호 문자열인지 판단하기 위한 함수
def is_right(s):
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True


def solution(p):
    answer = ''
    if p == '':
        return answer

    # 균형잡힌 괄호 문자열로 분할하기 위한 인덱스 찾기
    count_l = 0
    count_r = 0
    for i in range(len(p)):
        if p[i] == '(':
            count_l += 1
        else:
            count_r += 1
        if count_l == count_r:
            index = i
            break
    
    # 균형잡힌 괄호 문자열 2개로 분할
    u = p[:index + 1]
    v = p[index + 1:]

    if is_right(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer


print(solution("()))((()"))

