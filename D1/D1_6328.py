# 6328. [파이썬 프로그래밍 기초(1) 파이썬의 기본 구조와 기초 문법] 8. 함수의 기초 9
# 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
# 결과를 출력하는 프로그램을 작성하십시오.

random = list(map(str, input().split(", ")))

for i in range(len(random)):
    if len(random[i]) > len(random[i-1]):
        a = random[i]

print(a)