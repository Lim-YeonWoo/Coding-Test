'''
p.180
[Chap6] 정렬

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :

'''

n = int(input())

a = []
for i in range(n):
    name, score = input().split()
    a.append((name, int(score)))

a.sort(key=lambda x: x[1])

for i in range(n):
    print(a[i][0], end=" ")