'''
# [구현] 12-8 문자열 재정렬

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :

'''

data = input()

a = []
b = []
for i in range(len(data)):
    if not data[i].isdigit():
        a.append(data[i])
    else:
        b.append(int(data[i]))

a.sort()

for i in a:
    print(i, end="")
print(sum(b))
