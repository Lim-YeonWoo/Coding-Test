'''
p.300
[Chap10] 그래프 이론
3_도시 분할 계획

# 문제 설명 :
    어떤 마을에 집 있고 도로들 있다. (한 무방향 그래프)
    그 마을을 두개의 마을로 쪼개고 싶다. (그래프 두개로 쪼개기)
    이때 필요없는 도로들 다 없애고 싶다.
        두 마을 사이의 도로
        한 마을 안에서도 불필요한 도로

    단 마을에 집 한개 이상.
    단 마을 안에 집들은 연결되어 있어야함.

# 문제 풀이 :
    [MST]
    MST 구하고 나서 MST에서 가장 큰 비용 하나 빼기.
    그러면 MST가 두개 생길 것.

# 어려웠던 점 :

'''

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

# 간선 sort
edges.sort()

res = []
for edge in edges:
    c, a, b = edge

    # 사이클 안생기면 union
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res.append(c)

print(sum(res) - max(res))