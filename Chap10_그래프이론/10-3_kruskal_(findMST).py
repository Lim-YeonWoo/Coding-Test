'''
# Chap 10 그래프 이론
# 10-3 크루스칼 _ 최소신장트리(MST) 찾기

* 신장 트리 Spanning Tree
    : 어떤 그래프에 대해,
    모든 노드를 포함하면서,
    사이클이 존재하지 않는 (트리)
    부분 그래프

* 최소 신장 트리 Minimum Spanning Tree
    : 비용이 최소인 신장 트리
    : ex) 전체 도시가 연결되게 도로를 놔라. 단 비용은 최소.

* MST 찾는 알고리즘 = kruskal
    ****************
    1. 간선 데이터를 정렬 (오름차순)
        : 이 작업을 위해서, 그래프 입력받을때
          edges 배열에 (비용, 노드1, 노드2) 로 넣어둬야함 (첫번째인 비용을 기준으로 정렬한다)

    2. 간선 하나씩 확인하며
        사이클이 발생하지 않는 경우, MST에 포함 (union)
    ****************
'''

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())

edges = []
parent = [0] * (v+1)
for i in range(v+1):
    parent[i] = i

'''여기부터 시작'''
for i in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 비용을 기준으로 간선 정렬
edges.sort()

# 크루스칼 알고리즘 (MST 의 비용 구하기)
res = []

for edge in edges: # 모든 간선마다
    c, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 생기지 않으면 (부모가 다르면)
        union_parent(parent, a, b) # MST에 넣기 (union하기)
        res.append(c)

print(sum(res))

