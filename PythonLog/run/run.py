import sys
import math
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]
    distance = [[]]
    house_count = 0
    chicken_count = 0
    result = math.inf
    
    def mark_map():
        house_num = 1 
        chicken_num = -1 
        nonlocal house_count
        nonlocal chicken_count

        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:
                    graph[i][j] = house_num
                    house_num += 1
                elif graph[i][j] == 2:
                    graph[i][j] = chicken_num
                    chicken_num -= 1 

        house_num -= 1
        chicken_num += 1

        house_count = house_num 
        chicken_count = abs(chicken_num)

    def count_distance(i, j, chicken_num): 
        
        is_visited = [ [False for _ in range(N)] for _ in range(N)]
        queue = deque() 
        queue.append((i, j, 0))
        is_visited[i][j] = True 
        dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while queue:
            cur = queue.popleft()

            if graph[cur[0]][cur[1]] > 0: 
                house = graph[cur[0]][cur[1]] - 1
                distance[chicken_num-1][house] = cur[2]

            for d in dir: 
                nx = cur[0] + d[0] 
                ny = cur[1] + d[1] 
                nd = cur[2] + 1 

                if nx >= 0 and nx < N and ny >= 0 and ny < N and not is_visited[nx][ny]:
                    queue.append((nx, ny, nd))
                    is_visited[nx][ny] = True

    def find_min_sum(comb) -> int: 
        sum = 0 

        for i in range(house_count): 
            min_dist = math.inf 

            for j in comb:
                min_dist = min(distance[j-1][i], min_dist)

            sum += min_dist
        
        return sum

    mark_map()
    distance = [ [0 for _ in range(house_count)] for _ in range(chicken_count)]

    for i in range(N):
        for j in range(N): 
            if graph[i][j] < 0: 
                count_distance(i, j, abs(graph[i][j]))

    chickens = [x + 1 for x in range(chicken_count)]
    combs = list(combinations(chickens, M))

    for c in combs:
        result = min(find_min_sum(c), result)

    print(result)
solution()