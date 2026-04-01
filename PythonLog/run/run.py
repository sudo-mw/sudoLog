import sys

def solution():
    n = int(sys.stdin.readline())
    star = [ [' ' for _ in range(n * 2 - 1)] for _ in range(n)] 

    def divide_and_conquer(x_range, y_range):
        length = len(y_range)   
        next_length = int(length / 2)
        next_x_length = next_length * 2 - 1

        if length == 3: 
            mark_star(x_range, y_range)
        else: 
            middle_y = int((y_range[0] + y_range[-1]) / 2) + 1

            left_x_range = range(x_range[0], x_range[0] + next_x_length)
            right_x_range = range(x_range[0] + next_x_length + 1, x_range[-1] + 1)

            middle_x_range_start = int((left_x_range[0] + left_x_range[-1]) / 2) + 1
            middle_x_range_end = int((right_x_range[0] + right_x_range[-1]) / 2) + 1
            middle_x_range = range(middle_x_range_start, middle_x_range_end - 1)

            divide_and_conquer(middle_x_range, range(y_range[0], y_range[0] + next_length))
            divide_and_conquer(left_x_range, range(middle_y, middle_y + next_length))
            divide_and_conquer(right_x_range, range(middle_y, middle_y + next_length))
    
    def mark_star(x_range, y_range): 
        star[y_range[0]][x_range[2]] = '*'

        star[y_range[1]][x_range[1]] = '*'
        star[y_range[1]][x_range[3]] = '*'

        for x in x_range:
            star[y_range[2]][x] = '*'

    divide_and_conquer(range(n * 2 - 1), range(n))
    print('\n'.join(''.join(row) for row in star))

   
solution()