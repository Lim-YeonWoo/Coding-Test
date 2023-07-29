'''
# [그리디] 11-2 곱하기 혹은 더하기

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
    1도 곱하는 것보다는 더하는게 도움이 된다
'''

data = input()

res = 0
for i in range(len(data)):
    a = int(data[i])

    if a == 0 or res == 0 or a == 1 or res == 1:
        res += a
    else:
        res *= a

print(res)