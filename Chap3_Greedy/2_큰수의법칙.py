'''
p.92
[Chap3] 그리디
[2] 큰수의 법칙
'''

N, M, K = map(int, input().split())
input_list = list(map(int, input().split()))

input_list.sort(reverse=True)
first = input_list[0]
second = input_list[1]

for _ in range(M):
    cnt = M // (K+1)
    res = (first * K + second) * cnt

    res += first * (M % (K+1))

print(res)