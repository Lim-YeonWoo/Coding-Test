'''
p.223
[Chap8] DP
4_바닥공사

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
    dp인건 알겠는데 점화식을 못찾았다.
    f(n) = f(n-1) + 2f(n-2)

'''

n = int(input())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3
for x in range(3, n+1):
    dp[x] = (dp[x-1] + dp[x-2]*2) % 796796

print(dp[n])