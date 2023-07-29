'''
# [그리디] 11-5 볼링공 고르기

# 문제 설명 :

# 문제 풀이 :
    data[i] 부터 시작해서 tail에 data[i]랑 다른거 개수만큼 더하기
    O(N^2)

# 어려웠던 점 :

'''

n, m = map(int, input().split())
data = list(map(int, input().split()))

res = 0
for i in range(len(data)):
    tail = data[i+1:]
    cnt = len(tail) - tail.count(data[i])
    res += cnt

print(res)