# 6327. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 8
# 숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
# 정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

def square(n):
    print(f"square({n}) => {n*n}")

random = list(map(int, input().split(", ")))

for i in range(len(random)):
    square(random[i])