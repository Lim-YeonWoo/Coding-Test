'''
p.148
[Chap5] DFS & BFS
[3] 음료수 얼려 먹기

# 문제 설명 :
    2차원 배열에 0 또는 1 이 주어진다.
    0끼리 뭉친 덩어리의 개수 세기.

# 문제 풀이 :
    2차원 배열, 탐색 => 2차원 배열을 그래프 모양으로 바꿔서 DFS.

# 어려웠던 점 :
    DFS를 여러번 해야겠다는 건 생각했는데,
    모든 [r][c]를 시작점으로해서 DFS를 다 돌려볼 생각을 못했다.

    * 맨 처음 0을 만나면 거기서 DFS를 돌리고 (1만나면 중단하니까 0 덩어리까지만 DFS 가능)
      돌렸으면 해당 0 덩어리는 다 1이 된다 (방문표시)
    * 1을 만나면 그냥 return False다.
    * 그래서 dfs(x,y)를 다 돌렸을때 True인 것의 개수가 0덩어리개수가 된다.

    DFS는 재귀함수로 구현하니까, 종료조건과 정답조건만 잘 생각해주면 구현은 쉽다.
'''

# 입력 받기
N, M = map(int, input().split())

ice_map = []
for i in range(N):
    ice_map.append(list(map(int, input())))

# dfs 돌리기
def dfs(x,y):

    # 종료 조건 1 (위치가 올바르지 않을때)
    if not (0<=x and x<N and 0<=y and y<M):
        return False

    # 종료 조건 2 (이미 방문한 곳일때) (map==1인 걸 이미 방문했다고 생각하자)
    if ice_map[x][y] == 1:
        return False
    else:
        ice_map[x][y] = 1 # 방문처리
        dfs(x-1, y)  # 상
        dfs(x+1, y)  # 하
        dfs(x, y-1)  # 좌
        dfs(x, y+1)  # 우
        return True # 성공 조건


res = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            res += 1

print(res)