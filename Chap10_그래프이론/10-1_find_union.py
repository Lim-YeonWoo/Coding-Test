'''
# Chap 10 그래프 이론
# 10-1 서로소 집합 ( find & union )

* parent배열 자기자신으로 초기화

* union(a,b) : a와 b의 부모를 확인해서 같지 않으면
            (a<b라 가정) b의 부모를 a의 부모로 바꿔준다.

* find(a) : parent[a] == a면 자기자신이 젤 위에 있는 것 (그 집합의 대표)
                  parent[a] != a일 때 find(parent[a])를 재귀호출
'''

def find_parent(parent, a):
    if parent[a] != a :
        parent[a] = find_parent(parent, parent[a])

    return parent[a] #a로 바꿔서 한번 해보자

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드와 간선 개수 입력
v, e = map(int, input().split())

# parent 배열 자기자신으로 초기화
parent = [0]*(v+1)
for i in range(v+1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split()) # a, b 노드가 연결 되어 있다고 입력됨
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i), end=" ")

print(parent)