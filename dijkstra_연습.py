import heapq
INF = int(1e9)

graph = [ [] for _ in range(n+1)] #graph[a].append((b,c))
dist = [INF] * (n+1)
q = []

start = 0
#시작노드 처리 (시작노드는 주어진다)
dist[start] = 0
heapq.heappush(q, (0, start))

#우선순위 큐에서 꺼내기
while q:
    # 일단 하나 꺼내기
    dist, now = heapq.heappop(q)

    # 이미 방문한건 버리기
    if dist[now] < dist:
        continue
    # 방문 안한건 인접노드 갱신
    for i in graph[now]: #i엔 (인접노드, 거리)들어있음
        cost = dist[now] + i[1]

        if cost < dist[i[0]] :
            dist[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(dist)