import sys

def solution():
    city_count = int(sys.stdin.readline())
    travel_target_count = int(sys.stdin.readline())
    graph = [ list(map(int, sys.stdin.readline().split())) for _ in range(0, city_count) ] 
    travel_plan = list(map(int, sys.stdin.readline().split()))

    for i in range(city_count):
        graph[i][i] = 1

    for k in range(city_count):
        for i in range(city_count):
            for j in range(city_count): 
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1 

    result = "YES"

    for i in range(0, len(travel_plan) - 1):
        current = travel_plan[i] - 1
        next = travel_plan[i+1] - 1

        if graph[current][next] == 0:
            result = "NO" 
            break
    
    print(result)

solution()