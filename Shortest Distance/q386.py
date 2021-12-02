n, m = map(int, input().split())  # 학생 수(노드 수), 간선 수 입력

scoreList = []
for _ in range(m):
    a, b = map(int, input().split())
    scoreList.append([a, b, 1])   # 진출
    scoreList.append([b, a, -1])  # 진입

countList = []
for i in range(n):
    countList.append(0)

for i in range(n + 1):
    for j in range(len(scoreList)):
        # 진출 간선 카운트
        if scoreList[j][2] == 1:
            countList[scoreList[j][0]] += 1
        # 진입 간선 카운트
        else:
            countList[scoreList[j][1]] += 1
            scoreList[j][0]