'''
p.197
[Chap7] 이진탐색
2_부품찾기

# 문제 설명 : list1, list2 주어지고 list2의 원소들이 list1에 있는지 없는지 판별하는 문제

# 문제 풀이 :
    방법1) 순차탐색
    방법2) 이진탐색 : list1 정렬해두고 거기서 이진탐색
    방법3) 계수정렬처럼 전체 list 만들어두고 list1에 있는거 idx로 표시하고 list2에서는 전체 list조회만 하는.
          전체범위가 1,000,000이라 메모리 비효율적인듯
    방법4) 집합 자료형 이용
          list1을 집합으로 만들고 있는지 없는지 확인

# 어려웠던 점 :
    탐색이라 순차탐색과 이진탐색밖에 떠올리지 못했다.
    집합 자료형 이용했으면 좋았을 것 같다.
'''

'''
[방법2] 이진탐색으로 풀기
'''
n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

list1.sort()

def binary_search(a, target, start, end):
    while start<=end:
        mid = (start+end)//2
        if a[mid] == target:
            return mid
        elif a[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for data in list2:
    res = binary_search(list1, data, 0, n-1)

    if res != None:
        print("yes", end=" ")
    else:
        print("no", end=" ")

'''
[방법4] 집합으로 풀기
n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

list1_set = set(list1)

for data in list2:
    if data in list1_set:
        print("yes", end=" ")
    else:
        print("no", end=" ")
'''