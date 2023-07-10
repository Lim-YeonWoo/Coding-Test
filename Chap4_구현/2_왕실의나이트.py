'''
p.115
[Chap4] 구현
[2] 왕실의나이트
'''

input_data = input()
r = int(input_data[1])
c = ord(input_data[0]) - ord('a') + 1

#steps = [(-2,-1), (-1, -2), (1, -2) ... ] 이렇게 list of tuples로도 표현가능
dx = [+2, +2, -2, -2, -1, +1, -1, +1]
dy = [+1, -1, +1, -1, +2, +2, -2, -2]

ans = 0
x, y = r, c

# dx, dy 적용
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    # 허용 범위 아니면 패스
    if (nx>8 or nx<1 or ny>8 or ny<1):
        continue

    # 허용 범위면 갱신
    ans += 1

print(ans)