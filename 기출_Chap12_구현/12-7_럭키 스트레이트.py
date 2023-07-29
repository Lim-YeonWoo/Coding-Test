'''
# [구현] 12-7 럭키 스트레이트

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :

'''

data = input()

# 입력 데이터를 list 형태로 변경
a = []
for i in range(len(data)):
    a.append(int(data[i]))

mid = len(a)//2
head = sum(a[:mid])
tail = sum(a[mid:])

if head==tail:
    print("LUCKY")
else:
    print("READY")
