'''
# [구현] 12-11 뱀

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :

'''
from collections import deque

N = int(input())
graph = [[0]*N for _ in range(N)] # 0 비어있음, 1 몸, 2 사과

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    graph[r][c] = 2

L = int(input())
time_list = []
for _ in range(L):
    t, c = input().split()
    time_list.append((int(t), c))
time_list.sort(reverse = True)

clock = 0
move = 1

move_list = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 위(0) 오른쪽(1) 아래(2) 위(3)
hx, hy = 0, 0 #머리 위치
tx, ty = 0, 0 #꼬리 위치
while True:
    # 시간 증가
    clock += 1

    # 방향 따라 머리 이동
    dx, dy = move_list[move][0], move_list[move][1]
    hx, hy  = hx + dx, hy + dy
    print(clock, hx, hy)

    if 0<= hx < N and 0<= hy < N: # 범위 내라면
        if graph[hx][hy] == 2 : # 머리가 이동한 곳이 사과라면
            # 사과 먹기
            graph[hx][hy] = 1
        elif graph[hx][hy] == 1: # 머리가 이동한 곳이 몸이라면
            ans = clock
            break
        elif graph[hx][hy] == 0: # 머리가 이동한 곳이 비어있다면
            graph[hx][hy] = 1
            # 꼬리 당기기
            graph[tx][ty] = 0
            tx, ty = tx + dx, ty + dy

    else: # 범위 내가 아니라면
        ans = clock
        break

    # 방향 바꿀 시간이면 바꾸기
    if time_list: # 비어있지 않을때만 보기
        t, c = time_list[-1][0], time_list[-1][1]
    if t == clock:
        print("방향전환", move)
        time_list.pop()

        if c == 'D': # 오른쪽으로 90도
            move += 1
            move = move % 4
        elif c == 'L': # 왼쪽으로 90도
            move -= 1
            move = move % 4

print(ans)
