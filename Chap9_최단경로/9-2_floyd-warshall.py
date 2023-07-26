'''
# Chap 9. 최단경로
# 9-2. floyd-warshall
    : 모든 노드 ~ 모든 노드까지의 최단거리
    : O(N^3)
    : DP
    : 2차원 리스트 
    : graph = 인접행렬
    
    : 알고리즘
        1. 2차원 리스트 INF로 초기화
            graph = [ [INF] * (n+1) for i in range(n+1) ]
        
        2. 대각선은 0

        3. 나머지는 연결된 간선의 가중치 값으로 갱신
            graph[2][1]은 2번노드에서 1번노드로 가는 거리  
            
        4. for k in range(n+1): # k 만큼 반복하면서
              k포함하는 행,열 빼고
             대각선 빼고
             나머지 칸에 대해, k를 거쳐갈때 더 빨라진다면 갱신
             cf) 구현은 그냥 삼중반복문
'''

#  n , m = 노드 개수, 간선 개수
n, m = map(int, input().split())

# graph 2차원 배열 (다 INF, 대각선은 0으로 초기화)
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if i == j:
            graph[i][j] = 0

# graph 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# floyd-warshall 실행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 결과 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(INF, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()