'''
p.227
[Chap8] DP
5_효율적인 화폐 구성

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
     *** DP단원이 아니였으면 DP라고 생각하지 못했을 것 같다.

     *** N가지 화폐를 가장 적게 이용해 M원 만드는 방법
        경우1) 화폐끼리 서로 배수일때
            : [그리디] 가장 큰 돈을 가장 많이...

        경우2) 화폐끼리 서로 배수가 아닐때
            : [DP] dp[i] = i원을 만들기 위한 화폐 개수
              i부터 갱신해나가기.

    *** min 값으로 갱신해야되는데 특수한 케이스가 -1이라고 주어졌다면,
    그냥 특수케이스를 INF값(문제조건상 나올 수 없는 최댓값)으로 줘버리고
    그 값이 나올때 -1을 출력하면 된다.
'''

# 입력
n, m = map(int,input().split())
money_list=[]
for i in range(n):
    money_list.append(int(input()))

# dp 배열 초기화
dp = [-1] * 10001
for money in money_list:
    dp[money] = 1

# dp 배열 채워나가기
for i in range(m+1):
    if(dp[i] >= 1):
        for money in money_list:
            if dp[i+money] == -1: # 맨처음은 그냥 갱신
                dp[i+money] = dp[i] + 1
            elif (dp[i+money] > dp[i] + 1) : # 그 다음은 더 작으면 갱신
                dp[i+money] = dp[i] + 1

#print(dp)
print(dp[m])
