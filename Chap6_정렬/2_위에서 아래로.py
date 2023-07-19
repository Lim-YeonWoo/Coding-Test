'''
p.178
[Chap6] 정렬

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :

'''

n = int(input())

a = []
for i in range(n):
    temp = int(input())
    a.append(temp)

a.sort(reverse=True)

for i in a:
    print(i, end=" ")