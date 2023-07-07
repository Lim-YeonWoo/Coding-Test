'''
p.92
[Chap3] 그리디
[3] 숫자카드게임
'''

n, m = map(int, input().split())

res = 0
for i in range(n):
    row = list(map(int, input().split()))
    row_min = min(row)

    if row_min > res:
        res = row_min

print(res)