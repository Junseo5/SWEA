# 1933. 간단한 N 의 약수

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")