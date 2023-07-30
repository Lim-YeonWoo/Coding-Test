'''
# [구현] 12-9 문자열 압축

# 문제 설명 :

# 문제 풀이 :

# 어려웠던 점 :
    그냥 빡구현인데 테케는 다 맞는데
    코너 케이스에서 실패가 뜬다.
    근데 코너케이스를 못 찾겠다.

'''


def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):  # i개 단위로 자른다
        res = ""
        cnt = 1
        start = 0
        # i개 단위로 압출했을때의 문자열 길이를 구한다.
        while True:
            if start + 2 * i > len(s):
                break

            now = s[start:(start + i)]
            next = s[(start + i):(start + (2 * i))]

            if now == next:
                cnt += 1
            else:
                if cnt != 1:
                    res = res + str(cnt) + str(now)
                    cnt = 1
                else:
                    res = res + str(now)

            start += i

        # 맨 뒤 꼬리 부분 처리
        if cnt != 1:  # 단위 1 인데 ccc 로 끝난 경우 3c 출력
            res = res + str(cnt) + str(now)
        else:  # 그렇지 않은 경우는 남은 부분 다 출력
            res = res + str(s[start:])

            # print(res)

        # answer 갱신
        answer = min(answer, len(res))

    return answer