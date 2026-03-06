import sys
from collections import deque

def solution():
    input = [int(x) for x in sys.stdin.readline().split()]
    student_count = input[0]
    compare_count = input[1] 

    in_degree = [0 for _ in range(student_count + 1)]
    graph = [[] for _ in range(student_count + 1)]

    def read_graph(): 
        for _ in range(compare_count): 
            compare = sys.stdin.readline().split()
            first = int(compare[0])
            second = int(compare[1])
            in_degree[second] += 1
            graph[first].append(second)

    def topology_sort(): 
        queue = deque()
        sequence = [] 

        for i in range(1, student_count + 1):
            if in_degree[i] == 0: 
                queue.append(i)
                sequence.append(i)

        while queue: 
            cur = queue.popleft() 

            for next in graph[cur]: 
                in_degree[next] -= 1
                if in_degree[next] == 0: 
                    queue.append(next)
                    sequence.append(next)

        print(" ".join(map(str, sequence)))
    
    read_graph()
    topology_sort() 

solution()