'''
# [구현] 12-9 문자열 압축

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
    그냥 빡구현인데 테케는 다 맞는데
    코너 케이스에서 실패가 뜬다.
    근데 코너케이스를 못 찾겠다.

    s = "012345"
    print(s[1:8]) 이렇게 out of index여도 알아서 1:끝까지로 인식됨
    "12345" 출력됨
'''

def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):  # i개 단위로 자른다
        res = ""
        cnt = 1
        prev = s[0:i] ### 파이썬 indexing & slicing 이 좋은게 out of index여도 알아서 처리해줌.

        # i개 단위로 압출했을때의 문자열 길이를 구한다.
        for j in range(i, len(s), i):
            now = s[j:j+i]

            if prev == now:
                cnt += 1
            else:
                if cnt == 1:
                    res = res + str(prev)
                    prev = now
                else:
                    res = res + str(cnt) + str(prev)
                    prev = now
                    cnt = 1

        # 남은 꼬리 처리
        if cnt==1:
            res = res + str(prev)
        else:
            res = res + str(cnt) + str(prev)

        #print(res)

        # answer 갱신
        answer = min(answer, len(res))

    return answer