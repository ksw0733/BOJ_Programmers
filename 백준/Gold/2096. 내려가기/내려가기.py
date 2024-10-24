import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N = int(input())
    dp_max = [0] * 3
    dp_min = [0] * 3
    
    first_row = list(map(int, input().split()))
    dp_max = first_row[:]
    dp_min = first_row[:]
    
    for _ in range(N - 1):
        row = list(map(int, input().split()))
        
        new_dp_max = [0] * 3
        new_dp_min = [0] * 3
        
        new_dp_max[0] = row[0] + max(dp_max[0], dp_max[1])
        new_dp_max[1] = row[1] + max(dp_max[0], dp_max[1], dp_max[2])
        new_dp_max[2] = row[2] + max(dp_max[1], dp_max[2])
        
        new_dp_min[0] = row[0] + min(dp_min[0], dp_min[1])
        new_dp_min[1] = row[1] + min(dp_min[0], dp_min[1], dp_min[2])
        new_dp_min[2] = row[2] + min(dp_min[1], dp_min[2])
        
        dp_max = new_dp_max
        dp_min = new_dp_min
        
    print(max(dp_max), min(dp_min))