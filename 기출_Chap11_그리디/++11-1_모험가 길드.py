'''
# [그리디] 11-1 모험가 길드

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
    (첫시도)
        a[i] = i가 나온 개수
        답 = 시그마 a[i]//i
    (반례)
        1    2   3
        1명  3명  2명
        이렇게 있으면 내 풀이대로면 1+1+0 = 2 인데
        2에서 남은 한명으로 3명 그룹 하나 더 만들 수 있으니까 답은 3이다.

    (정답)
        입력 list 정렬
        for문 돌면서, 해당 수만큼 개수 세면서 그룹 만들기.
'''

n = int(input())
data = list(map(int,input().split()))

data.sort()

res = 0
tmp = 0
for i in range(len(data)):
    tmp += 1 # 현재 그룹에 data[i]를 포함시킴

    if tmp >= i : # 현재 그룹 인원수가 공포도만큼이 됐다면
        res += 1
        tmp = 0

print(res)