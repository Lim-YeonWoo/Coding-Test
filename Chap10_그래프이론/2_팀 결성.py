'''
p.298
[Chap10] 그래프 이론
2_팀 결성

# 문제 설명 :


# 문제 풀이 :
    전형적인 union & find 문제

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

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    oper, a, b = map(int, input().split())

    if oper == 0: # union
        union_parent(parent, a, b)
    else: # find
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a==b:
            print("YES")
        else:
            print("NO")