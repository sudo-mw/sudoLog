from bisect import bisect_left
import sys

def solution(): 
    first = sys.stdin.readline().strip()
    second = sys.stdin.readline().strip()
    col_size = len(first)
    row_size = len(second)
    dp = [ [0 for _ in range(col_size + 1)] for _ in range(row_size + 1) ] 

    for i in range(1, row_size + 1):
        for j in range(1, col_size + 1):
            if second[i-1] == first[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[row_size][col_size])

solution()