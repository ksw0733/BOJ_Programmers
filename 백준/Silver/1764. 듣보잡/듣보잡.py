import sys
input = sys.stdin.readline

def solution(n, m):
    people = {}
    for _ in range(n+m):
        name = str(input().rstrip())
        if name not in people:
            people[name] = 1
        else:
            people[name] += 1
    res = sorted([k for k, v in people.items() if v == 2])
    return len(res), res
                
if __name__ == "__main__":
    n, m = map(int, input().split())
    ans, name = solution(n, m)
    print(ans)
    for name in name:
        print(name)