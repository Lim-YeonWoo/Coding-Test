'''
p.197
[Chap7] 이진탐색
3_떡볶이 떡 만들기

# 문제 설명 :

# 문제 풀이 :
    내 풀이) 이진탐색을 쓰면서 순차탐색도 씀... 시간복잡도 크다.
        data_list.sort(reverse=True)
        for x in range(min(data_list)~max(data_list):
            x가 들어갈 idx 찾기 (by 이진탐색 이용한 라이브러리인 bisect)
            [0:idx]로 slicing한걸 a라 하자
            res = sum(a) - x*len(a)
            if res == 요구한 길이:
                print(x)
                break

# 어려웠던 점 :
    *** 어디에 이진탐색을 적용해야하는지 한번에 판단하기 어려웠다

    *** [이진탐색]
        아래 내용 아님. 라이브러리 써서 되는 문제는 라이브러리쓰고 아닌 문제는 다 binary_search 코드 변형해서 푸는 것.
        binary_search도 정확한값 말고 최대한 가까운값 등 찾는거 가능.
        1) [1 2 4 5]에서 4의 idx 찾기
        이진 탐색에서 정확하게 target값을 찾는 것 => [[binary_search 구현]]

        2) [1 2 4 5]에서 3이 들어갈 idx 찾기
        이진 탐색에서 target이 들어갈 idx를 찾는 것 => [[bisect 라이브러리 이용 가능]]

    *** [bisect 라이브러리]
        from bisect import bisect_left, bisect_right
        bisect_left(a, x)

        이때 a 가 오름차순으로 정렬된 상태여야 올바른 답을 도출한다. (내림차순 정렬도 안됨)
'''

'''
[정답 풀이]
'''
n, m = map(int, input().split()) #n은 list 길이, m은 요청한 길이
data_list = list(map(int, input().split()))

start = 0
end = max(data_list)

# 이진 탐색
while start<=end:
    mid = (start+end)//2

    # 잘릴 떡의 양 계산
    res = 0
    for i in data_list:
        if i > mid:
            res += (i-mid)

    # 결과 판단
    if res == m:
        print(mid)
        break
    elif res < m:
        end = mid - 1
    else:
        start = mid + 1

'''
[내 풀이]

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
'''
