'''
# [구현] 11-6 무지의 먹방 라이브

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
    주어진 문제상황 그대로 [구현]했는데 그러면 시간초과.
    [그리디]로 문제상황 이해하고 바꿔서 다르게 구현해야함.
'''

''' 
방법1 : 구현 
이대로 풀면 효율성 테스트가 0점 나와서 반타작이다.

def find_next(food_times, now):
    if now == len(food_times) - 1:
        next = 0
    else:
        next = now + 1
    return next

def solution(food_times, k):
    now = 0

    for _ in range(k):  # k 초 까지 무지 먹이기
        food_times[now] -= 1  # now 음식 먹음
        #print(now+1, food_times)

        flag = False
        for _ in range(len(food_times)): # food_times번 만큼 확인
            next = find_next(food_times, now)

            if food_times[next] > 0 : # 먹을 수 있는 next 찾으면 next 확정
                flag = True
                now = next
                break
            else:
                now = next

        if flag == False:
            return -1

    return now+1
'''

''' 방법2. 그리디'''