def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)   
    """
    3을 곱하는 이유는 numbers의 원소가 1000이하로 3자리수까지 비교해야 되기때문
    3과 31이 있을때 문제 조건에 맞는 큰수가 되려면 3이 31보다 앞에와야 하지만
    sort를 사용하면 31이 앞에오게됨 하지만 *3을 하여 333과 313131이 있으면 3이 앞으로 정렬되어
    문제의 조건에 부합하게 됨
    """
    return str(int(''.join(numbers)))