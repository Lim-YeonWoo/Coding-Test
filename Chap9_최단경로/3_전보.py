'''
p.262
[Chap9] 최단경로
3_전보

# 문제 설명 :
    시작 노드 주고
    시간 충분히 줬을때, 최종적으로 도착할 수 있는 노드는 몇개이며, 얼마나 걸리는가.

# 문제 풀이 :
    다익스트라.
    시작노드로부터 최단거리 구한 distance배열에서 -1이 아닌 개수 출력 && max(distance) 출력

# 어려웠던 점 :

'''
INF = int(1e9)
import heapq

n, m, start = map(int, input().split())

q = []
graph = [[] for _ in range(n+1)]
distance= [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
def dijkstra(start):
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q :
        dist, now = heapq.heappop(q)

        # 이미 방문한 것은 무시
        if distance[now] < dist:
            continue

        # 방문 안했던 것은 (1) 인접 노드 거리 갱신 && (2) 갱신된 노드 q에 넣기
        for i in graph[now]: # i는 (노드, 거리)
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

res1 = 0
res2 = 0
for i in range(1, n+1):
    if distance[i] != INF:
        res1 += 1
        res2 = max(distance[i], res2)

print(res1-1, res2) # start 노드는 개수 빼줘야함