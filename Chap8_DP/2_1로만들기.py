'''
p.217
[Chap8] DP
2_1로만들기

# 문제 설명 :

# 문제 풀이 :
    (첫시도) greedy로 /5 /3 /2 -1 순차적으로 하려함
    10 -> 5 -> 4 -> 2 -> 1
    10 -> 9 -> 3 -> 1
    같은 반례 존재

    (다른 시도) dp, top-down (재귀호출)

    (책 정답) dp, bottom-up (반복문)

# 어려웠던 점 :
    dp 문제일 경우 그래프 그려보고
    점화식으로 써보고
    그걸 구현하자
'''

n = int(input())
dp = [0] * 30001 # dp[i] = i수에 대한 계산 횟수

def cnt(i):
    # 재귀 종료 조건
    if i == 1:
        return 0

    # dp값 탐색 (메모이제이션)
    if dp[i] != 0:
        return dp[i]

    res = []
    res.clear()
    if i % 5 == 0:
        res.append(cnt(i//5))

    if i % 3 == 0:
        res.append(cnt(i//3))

    if i % 2 == 0:
        res.append(cnt(i//2))

    res.append(cnt(i-1))

    dp[i] = min(res) + 1
    return dp[i]

print(cnt(n))