def solution(s):
    s = s.lower()
    d = {'p': 0, 'y': 0}
    for a in s:
        if a == 'p':
            d[a] += 1
        if a == 'y':
            d[a] += 1
    if d.get('p') == d.get('y'):
        return True
    else:
        return False