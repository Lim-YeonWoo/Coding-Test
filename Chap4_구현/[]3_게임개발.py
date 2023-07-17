'''
p.118
[Chap4] 구현
[3] 게임개발

# 문제 설명 :

# 문제 풀이 :
    시뮬레이션. 구현.
    상하좌우 탐색.

# 어려웠던 점 :
    문제에서 요구하는거 자체가 길어서 구현하는데 시간이 오래 걸렸다.
'''

# 입력
N, M = map(int, input().split())
x, y, view = map(int, input().split())

m = []
for i in range(N):
    m.append(list(map(int, input().split())))

# 탐색
ans = 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m[x][y] = 1
while True:
    # 4방면 탐색
    for i in range(4):
        view = (view - 1) % 4
        nx = x+dx[view]
        ny = y+dy[view]
        flag = False #새로 이동한거면 True

        if (m[nx][ny] == 0) : #육지이면
            x, y = nx, ny #위치 갱신
            m[x][y] = 1 #방문했다고 표시(바다로 갱신)
            ans += 1 #방문한 칸 개수 갱신
            print(x,y)
            flag = True
            break

    # 새로 이동하지 않았으면 뒤로 한칸 이동
    if flag == False:
        nx = x - dx[view]
        ny = y - dy[view]

        if m[nx][ny] == 1 : #바다이면
            print(ans)
            break
        else:
            x, y = nx, ny
            m[x][y] = 1
            print(x, y)
            continue