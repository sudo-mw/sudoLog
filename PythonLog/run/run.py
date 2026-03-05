import sys
from collections import deque
import math

def solution(): 
    map_meta = sys.stdin.readline().split()
    row_size = int(map_meta[0])
    col_size = int(map_meta[1])

    map = [ [int(x) for x in sys.stdin.readline().strip()] for _ in range(row_size) ]
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # is_visted[1][2][3] 0번 인덱스에서 0은 벽을 부수지 않은 채 이동, 1은 부순 채 이동
    distance = [ [ [math.inf for _ in range(col_size) ] for _ in range(row_size) ] for _ in range(2) ] 
    queue = deque()

    queue.append((0, 0, 0, 1))
    distance[0][0][0] = 1

    while queue: 
        current = queue.popleft()

        for d in dir:
            nr = current[1] + d[0]
            nc = current[2] + d[1] 

            if nr >= 0 and nr < row_size and nc >= 0 and nc < col_size: 
                if map[nr][nc] == 0 and distance[current[0]][nr][nc] == math.inf: 
                    queue.append((current[0], nr, nc, current[3] + 1))
                    distance[current[0]][nr][nc] = current[3] + 1
                elif map[nr][nc] == 1 and current[0] == 0 and current[3] + 1 < distance[1][nr][nc]: 
                    queue.append((1, nr, nc, current[3] + 1))
                    distance[1][nr][nc] = current[3] + 1

    min_dist = min(distance[0][row_size-1][col_size-1], distance[1][row_size-1][col_size-1])
    print(min_dist if min_dist > 0 and min_dist != math.inf else -1)        

solution()