'''
p.259
[Chap9] 최단경로
2_미래도시

# 문제 설명 :
    그래프 있고, 1도시 -> K도시 -> X도시 갈때 최소시간

# 문제 풀이 :
    INF, 0, 1 로 2차원 배열 초기화
    플로이드워셜
    graph[1][K] + graph[K][X] 가 답

# 어려웠던 점 :
    간선개수, 노드개수 <= 100 으로 작으므로
    O(N^3)인 플로이드워샬 이용 가능
'''

# 노드개수, 간선개수
n, m = map(int, input().split())

INF = int(1e9)
graph = [ [INF]*(n+1) for _ in range(n+1) ]

# 대각선 0으로 초기화
for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

# graph input 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1 # 양방향 그래프라!!!

# 플로이드 워샬
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b] , graph[a][k] + graph[k][b])

# 경유지, 도착지
X, K = map(int, input().split())

res = graph[1][K] + graph[K][X]
if res >= INF:
    print(-1)
else:
    print(res)