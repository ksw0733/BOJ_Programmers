import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    s = set()
    for _ in range(n):
        commands = input().rstrip().split()
        if len(commands) == 1:
            if commands[0] == 'all':
                s = set(list(range(1, 21)))
            else:
                s = set()
        else:
            command, num = commands[0], int(commands[1])
            if command == 'add':
                s.add(num)
            elif command == 'remove':
                s.discard(num)
            elif command == 'check':
                print(1 if num in s else 0)
            else:
                if num in s:
                    s.remove(num)
                else:
                    s.add(num)