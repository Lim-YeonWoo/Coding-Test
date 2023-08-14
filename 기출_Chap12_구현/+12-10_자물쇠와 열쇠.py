'''
# [구현] 12-10 자물쇠와 열쇠

# 문제 설명 :

# 문제 풀이 :
    구현-완전탐색 으로 다 구현해보면 어떨까 시간복잡도 계산해봄 ( O(400*400*4방면) 이라 괜찮다 판단)

    내 풀이) 자물쇠0에 열쇠1하나 딱맞게 주고 그걸 기준으로 rotate 4번 반복.
        translation 먼저, rotate 나중.
        (생각해보니까 무언가를 기준으로 rotate할려면 그 안에서 또 translatoin이 들어가므로
        rotate 먼저하고, 그리고 나서 translation으로 딱맞게 기준주는게 좋을듯)

    교재 풀이) rotate 1개 마다 한칸씩 움직여봄.
        rotate 먼저, translation 나중.

        배열이 움직일수 있는 영역 만큼 배열 확장 시켜두고,
        나중에 true인지 아닌지 판단할때는 원래 배열 영역만큼만 확인하는 방법.

# 어려웠던 점 :
    * 행렬 90도 회전
        m행 n열이라면
        res = [[0]*m for _in range(n)] 으로 n행 m열로 초기화

        [r][c] -> [c][row_len -r -1]
        res[c][row_len - r - 1] = original[r][c]

    * set 자료형
        set.add(1) # 한개 추가
        set.update([2,3]) # 여러개 추가
        set.remove(4) # 제거

        setA == setB 같은 연산 가능.

    *** 코너 케이스
        lock이 모두 1일때 그런 경우는 예외 처리 해줘야함.
'''

def rotate_matrix(a):
    row_len = len(a)
    col_len = len(a[0])
    res = [[0]*row_len for _ in range(col_len)]

    for r in range(row_len):
        for c in range(col_len):
            res[c][row_len - r -1] = a[r][c]

    return res

def solution(key, lock):
    answer = False

    # 입력 형태 set으로 바꾸기 (lock)
    lock_set = set()
    lock_row = len(lock)
    lock_col = len(lock[0])
    for r in range(lock_row):
        for c in range(lock_col):
            if lock[r][c] == 0:
                lock_set.add((r,c))
    if len(lock_set) == 0 : # 이미 처음부터 다 1이라 열 수 있음
        return True

    # rotate
    for _ in range(4):
        # rotate the key
        key = rotate_matrix(key)
        '''print("key", key)'''

        # 입력 형태 set으로 바꾸기 (key)
        key_set = set()
        for r in range(len(key)):
            for c in range(len(key[0])):
                if key[r][c] == 1:
                    key_set.add((r,c))
        ''' print("key_set", key_set)'''

        # key_set의 값을 lock_set 값 중 하나에 맞게 translation
        for x in lock_set: # x 가 기준
            for y in key_set: # key_set의 y를 x에 맞추기
                dx, dy = x[0]-y[0], x[1]-y[1]
                TRkey_set = set()

                for i in key_set: # key_set translation
                    nx, ny = i[0]+dx, i[1]+dy
                    if 0<= nx < lock_row and 0<= ny < lock_col:
                        TRkey_set.add((nx, ny))
                '''print("===============")
                print("lock 기준", x)
                print("맞춘 key", y)
                print(dx, dy)
                print("TRkey_set", TRkey_set)
                print("lock_set", lock_set)'''

                # 열 수 있나 없나 확인
                if lock_set == TRkey_set:
                    answer = True
                    return answer
    
    return answer