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

    '''여기 추가 해줘야 N이 클때 시간 단축가능'''
    if N < K: #이미 N이 K보다 작아서 나눠떨어질 수 없을때는 -1을 반복하며 count하지말고 한번에 계산
        cnt += N-1

    if N%K==0:
        N = N//K ###int형으로 만들려면 // 써야함을 주의
        cnt += 1
    else:
        N = N-1
        cnt += 1
print(cnt)