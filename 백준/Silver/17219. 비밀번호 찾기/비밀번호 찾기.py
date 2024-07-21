import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    site_password = {}
    for _ in range(n):
        site, password = map(str, input().rstrip().split())
        site_password[site] = password
    
    for _ in range(m):
        print(site_password[input().rstrip()])