'''
p.197
[Chap7] 이진탐색
3_떡볶이 떡 만들기

# 문제 설명 :

# 문제 풀이 :
    내 풀이)
        data_list.sort(reverse=True)
        for x in range(min(data_list)~max(data_list):
            x가 들어갈 idx 찾기 (by 이진탐색 이용한 라이브러리인 bisect)
            [0:idx]로 slicing한걸 a라 하자
            res = sum(a) - x*len(a)
            if res == 요구한 길이:
                print(x)
                break

# 어려웠던 점 :
    *** [이진탐색]
    1) [1 2 4 5]에서 4의 idx 찾기
    이진 탐색에서 정확하게 target값을 찾는 것 => [[binary_search 구현]]

    2) [1 2 4 5]에서 3이 들어갈 idx 찾기
    이진 탐색에서 target이 들어갈 idx를 찾는 것 => [[bisect 라이브러리 이용]]

    *** [bisect 라이브러리]
    from bisect import bisect_left, bisect_right
    bisect_left(a, x)

    이때 a 가 오름차순으로 정렬된 상태여야 올바른 답을 도출한다. (내림차순 정렬도 안됨)
'''

from bisect import bisect_left, bisect_right

n, m = map(int, input().split()) #n은 list 길이, m은 요청한 길이
data_list = list(map(int, input().split()))

data_list.sort()

for x in range(max(data_list)-1, -1, -1):
    idx = bisect_right(data_list, x)
    a = data_list[idx:]
    res = sum(a) - x * len(a)
    if res >= m: #잘린 떡의 총합이 요구한 길이와 같다면
        print(x)
        break