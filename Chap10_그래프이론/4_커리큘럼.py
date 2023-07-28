'''
p.303
[Chap10] 그래프 이론
4_커리큘럼

# 문제 설명 :
    선수과목 있고
    각 과목마다 수강 시간 정해져있을때
    과목1 30시간 필요, 과목2 20시간 필요, 과목3 40시간 필요
    이때 과목3의 선수과목이 과목1,과목2라면,
    과목1 & 과목2 듣는데 max(30,20)=30이라 30시간 필요.
    따라서 과목3은 총 30 + 40 = 70 시간 필요.

    각 과목마다 필요한 시간 출력

# 문제 풀이 :
    첫시도) [위상정렬]
        진입차수 0 인 노드에 연결된 간선 지울때
        a -> b 라면
        b수강시간 < a수강시간 이면 ((선수과목이 두개 이상일때 고려함))
        b수강시간 += a수강시간
    반례)
        선수과목1 30, 선수과목2 20, 과목 40
        30 < 40 이라 안더해짐
        20 > 40 이라 더해짐
    고민)
        진입차수 중에 max 값을 더해야하는 데 어떻게 max를 찾아서 더하지?

    시도2) [위상정렬]
        그래프 입력받을때 그 노드의 indegree만 계산해두는게 아니라
        해당 노드로 들어오는 간선의 max값도 구해두면 되지 않나?


    정답풀이)


# 어려웠던 점 :
    진입차수 중에 max 값을 더해야하는 데 어떻게 max를 찾아서 더하지?
'''
from collections import deque

n = int(input())

indegree = [0] * (n+1)
time = [0] * (n+1)
time2plus = [0] * (n+1) # 이따 더해야할 숫자를 저장해두는 배열 (바로 안 더하는 이유는 최댓값 찾으려고)
graph = [[] for _ in range(n+1)]

# 그래프 정보 입력 받으면서 indegree 계산 해두기
for i in range(1, n+1):
    data = list(map(int, input().split()))

    time[i] = data[0]

    for x in range(1, len(data)-1): # (data[i] -> node1, 비용 없음)
        graph[data[x]].append(i)
        indegree[i] += 1

# 맨 처음에는 순차탐색하면서 진입차수 0 인거 q에 넣기
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

# 큐 빌 때까지 돌기
topology_res_list = []
while q:
    print(topology_res_list)
    now = q.pop()
    topology_res_list.append(now)
    time[now] += time2plus[now]

    for i in graph[now]: # i는 now노드랑 연결된 (->) 노드 들어있음
        indegree[i] -= 1
        time2plus[i] = max(time2plus[i], time[now])

        if indegree[i] == 0:
            q.append(i)

print(topology_res_list)
print(time)