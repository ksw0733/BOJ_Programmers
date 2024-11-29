import sys
from itertools import combinations
input = sys.stdin.readline

def calculate_chicken_distance(house, chicken_comb):
    total_distance = 0
    for x, y in house:
        min_distance = float('inf')
        for cx, cy in chicken_comb:
            min_distance = min(min_distance, abs(x-cx) + abs(y-cy))
        total_distance += min_distance
    return total_distance

def solution(city, N, M):
    house = []
    chicken = []
    
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append((i, j))
            elif city[i][j] == 2:
                chicken.append((i, j))
    
    chicken_combinations = combinations(chicken, M)
    
    min_chicken_distance = float('inf')
    for chicken_comb in chicken_combinations:
        city_distance = calculate_chicken_distance(house, chicken_comb)
        min_chicken_distance = min(min_chicken_distance, city_distance)
    
    return min_chicken_distance

if __name__ == '__main__':
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    print(solution(city, N, M))
    