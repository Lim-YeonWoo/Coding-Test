'''
p.182
[Chap6] 정렬

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :

'''

n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

'''
이미 바꾼 앞부분은 더이상 볼 필요가 없으므로
매번 바꿀때마다 sorting할 필요가 없다.
k번 반복 시작하기 전에 한번만 sorting해주면 된다.
'''
'''
for i in range(k):
    a.sort()
    b.sort(reverse=True)

    if a[0] < b[0]:
        a[0], b[0] = b[0], a[0]
    else:
        break
'''
a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))
