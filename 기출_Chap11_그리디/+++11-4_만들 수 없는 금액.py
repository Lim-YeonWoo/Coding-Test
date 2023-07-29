'''
# [그리디] 11-4 만들 수 없는 금액

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
    *** 방법을 생각해내는게 너무 어려웠다
    *** 가진 동전을 sort해두고
        i번째동전까지만 가졌다고 생각하고 만들 수 있는 돈 구하기 (1 ~ end)
        그다음 동전 추가했을때 만들 수 있는 돈 갱신 (1 ~ end+그다음동전)

'''

n = int(input())
data = list(map(int, input().split()))

data.sort()

end = 1
for i in data:
    if end < i :
        print(end)
        break

    end += i