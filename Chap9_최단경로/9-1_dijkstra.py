'''
*****중요. 암기할 것.

# Chap 9 최단경로
# 9-1. dijkstra
    : start노드에서 나머지 다른 노드까지의 최단거리
    : 음의 간선 없을 때
    : 그리디 알고리즘 중 하나
    : 1차원 리스트 distance에 거리 저장
    : heapq를 이용한 우선순위큐 이용 -> O(ElogV)
    : 노드가 V개 있다면, 가장 짧은 최단거리 가지는 노드 찾아서 갱신하는 과정을 V번 함.
      한 단계마다 now노드에 대한 최단거리는 확실히 찾는다.

    : 알고리즘
        0. 우선순위 큐 선언
            import heapq
            q = []

        0. 인접노드 저장할 2차원 배열 graph
            graph = [ [] * for i in range(n+1) ]

        1. distance = [INF] * (n+1) 로 초기화
            distance[start] = 0
            heapq.heappush(q, (0, start))

        2. 가장 짧은 최단거리 가진 now 노드 선택 (맨처음엔 start 노드가 선택됨)
            dist, now = heapq.heappop(q)

            1) now노드 이미 방문 했으면 무시
            2) now노드 방문 안했으면
                * 인접노드 갱신
                * 갱신된 노드는 heapq에 push

        3. 우선순위 큐가 빌 때까지 2 반복
'''
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한

# 노드 개수, 간선 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 입력 받기
start = int(input())

# graph
graph = [ [] for _ in range(n+1)]
# graph 입력 받기
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) # a노드에서 b노드로 가는 비용이 c

# 다익스트라 시작
distance = [INF] * (n+1)
q = []
def dijkstra(start):
    # 시작노드 초기화
    distance[start] = 0
    heapq.heappush(q, (0, start))

    # 반복 시작
    while q:
        dist, now = heapq.heappop(q)

        # 이미 방문 했다면 무시
        # 방문했었다면 distance배열에 들어있는 값이, 큐에 들어있는 값보다 작을 것
        if distance[now] < dist:
            continue

        # 방문 하지 않았다면
        for i in graph[now]: # i 에는 (인접노드, 거리)가 들어있음
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 실행 & 결과 출력
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("도달할 수 없음")
    else:
        print(distance[i])