'''
# [그리디] 11-3 문자열 뒤집기

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :

'''

data = input()

now = data[0]
cnt = 0

for i in range(1, len(data)):
    if data[i] != now:
        cnt += 1
        now = data[i]

print((cnt+1)//2)
