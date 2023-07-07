'''
p.92
[Chap3] 그리디
[4] 1이될때까지
'''

N, K = map(int, input().split())
cnt = 0
while True:
    if N==1:
        break

    if N%K==0:
        N = N//K
        cnt += 1
    else:
        N = N-1
        cnt += 1
print(cnt)