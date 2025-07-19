# 6326. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 7
# 다음과 같이 팩토리얼을 구하는 함수를 정의해 입력된 숫자에 대한
# 팩토리얼 값을 구하는 프로그램을 작성하십시오.

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        
    print(result)

random = int(input())
factorial(random)
