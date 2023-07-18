'''
p.152
[Chap5] DFS & BFS
[4] 미로 탈출

# 문제 설명 :
    [0][0]에서 출발해서 1인 부분만 지나 [N][M]에 도달할 수 있는 최단거리.
    (그럴 수 있는 길이 없는 경우는 주어지지 않는다)

# 문제 풀이 :
    2차원배열의 탐색 => DFS, BFS

# 어려웠던 점 :
    "최단거리"임을 어떻게 구할지 모르겠다.
    => (정답코드) map 자체에 (여태까지의 거리)를 저장하였다. ex) map[1][2] = 3
       즉, 방문표시를 0과 1 로 하지않고, 방문안했으면 0 방문했으면 거리(0초과)를 넣었다
'''

from collections import deque

N, M = map(int, input().split())

my_map = []
for i in range(N):
    my_map.append(list(map(int, input())))

# 상하좌우
dx = [-1, +1, 0, 0]
dy = [0, 0, -1, +1]

def bfs(x,y): #시작점 (x,y)=(0,0)이 된다
    # [0] 큐 생성 & 시작점 넣기 & 방문 표시
    q = deque([(x,y)])
    my_map[x][y] = 1 # 한칸 방문 했으니까 거리=1

    # [1] 큐 빌 때까지 반복
    while q :
        # [1-1] 큐에서 빼기
        (x, y) = q.popleft()
        #print(x,y)
        
        # [1-2] 이웃하는 모든 노드 중 방문 안한거 큐에 넣기
        for i in range(4): # 이웃하는 모든 노드에 대해 (여기선 상하좌우가 이웃하는 노드)
            nx = x + dx[i]
            ny = y + dy[i]

            if (0<=nx and nx<N and 0<=ny and ny<M): # 정상 범위인지 확인
                if my_map[nx][ny] == 1: # 방문 안한 노드인지 확인
                    my_map[nx][ny] = my_map[x][y] + 1 # my_map에 거리로 방문 표시
                    q.append((nx, ny)) # q에 넣기
                    '''이때 여기서 x,y를 함부로 갱신하면 안됨. for문 돌때 x,y가 고정이어야함'''

bfs(0, 0)
print(my_map[N-1][M-1])
