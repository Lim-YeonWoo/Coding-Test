'''
# Chap 10 그래프 이론
# 10-2 그래프의 사이클 존재 여부 판단하기 by find() & union()

!! 무방향 그래프 !! 의 사이클 판별

Algorithm:
모든 간선에 대해
    각 간선 양끝에 달린 노드 a,b에 대해
    a, b의 부모가 같으면
        cycle 생긴거.
        break.
    a, b 부모 다르면
        union연산 해주기. (같은 무리에 뭉쳐있으니까)


=> 모든 간선에 돌았는데 break안됐으면 cycle 없는거.
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

''' 여기부터 시작 '''
isCycle = False
for i in range(e): # 모든 간선에 대해
    # 간선 정보 입력 받기
    a, b = map(int, input().split()) # a, b 노드가 연결되어있다는 뜻.

    if find_parent(parent, a) == find_parent(parent, b):
        isCycle = True
        break
    else:
        union_parent(parent, a, b)

print(isCycle)
