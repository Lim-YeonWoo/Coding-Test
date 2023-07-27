'''
# Chap 10 그래프 이론
# 10-4 위상 정렬 Topology Sort

방향 그래프의 모든 노드를, 방향성에 거슬리지 않도록 순서대로 나열하는 것

* 집입차수 indegree
    : 그래프에서 어떤 노드에 들어오는 간선의 개수
    : 그래프에서 v, e 정보 입력 받을때 indegree 계산 해둬야함

* 위상 정렬 Topology Sort
약간 더 게임오브데스 하듯...
진입차수 0인 노드 (젤 꼭데기의 노드) 제거
거기서 출발하는 화살표 없애기...

Algorithm
1. 집입차수가 0인 것을 queue에 넣는다.
2. queue가 빌 때 까지 반복
    queue에서 꺼낸 원소
        : 그 원소에서 출발하는 간선 제거
        : 그 원소랑 연결되는 노드들의 indegree가 변했을 거임.
            새롭게 indegree가 0 된거 q에 넣기
3. q에서 꺼낸 순서가 곧 위상 정렬

* 위상 정렬의 답은 여러개가 가능하다는 것이 특징
* 모든 원소를 방문하기 전에 큐가 빈다는 것은 사이클이 발생한 것. (사이클이 발생하면 그 어느 것도 큐에 들어갈 수 없음. 진입차수가 0이 안될거니까)
'''

from collections import deque

v, e = map(int, input().split())

# indegree 1차원 배열
indegree = [0] * (v+1)
# graph 2차원 배열 (인접 리스트)
graph = [ [] for _ in range(v+1)]

# 입력 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    indegree[b] += 1 # 그래프 정보 입력 받을때 indegree 이미 계산해둬야함

'''def topology_sort():'''
q = deque()
res = []

# 맨 처음에는 순차탐색하면서 진입차수 0인거 q에 넣기
for i in range(1, v+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    res.append(now)

    for i in graph[now]: # i 는 (now랑 연결된 노드, 비용)
        indegree[i[0]] -= 1 # indegree 갱신

        if indegree[i[0]] == 0:
            q.append(i[0])

print(res)

