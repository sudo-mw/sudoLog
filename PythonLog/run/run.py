import sys

def solution():
    bounds = list(map(int,sys.stdin.readline().split()))
    min_r = bounds[0]
    min_c = bounds[1]
    max_r = bounds[2] + 1
    max_c = bounds[3] + 1
    max_length = 0 
    result = [[]]

    def find_value(r, c) -> int: 
        max_coordinate = max(abs(r), abs(c))
        min_coordinate = max_coordinate * -1
        length = max_coordinate * 2 + 1
        base = max_coordinate * 2 + 1
        start_value = base * base

        if r == max_coordinate and c == max_coordinate:
            return start_value
        elif r == max_coordinate: 
            diff = max_coordinate - c
            return start_value - diff 
        elif c == min_coordinate: 
            value = start_value - length + 1
            diff = max_coordinate - r
            return value - diff 
        elif r == min_coordinate:
            value = start_value - (length * 2) + 2
            diff = abs(min_coordinate - c)
            return value - diff 
        else:
            value = start_value - (length * 3) + 3 
            diff = abs(r - min_coordinate)
            return value - diff

    for (i, r) in enumerate(range(min_r, max_r)):
        for (j, c) in enumerate(range(min_c, max_c)):
            value = find_value(r, c)
            result[i].append(value)
            max_length = max(max_length, len(str(value)))
        result.append([])

    result.pop()
    print('\n'.join(' '.join(f"{v:>{max_length}}" for v in row) for row in result))

solution()