# 입력 n에 대한 n! 출력

n = int(input('n:'))
result = 1
while True:
    result = result*n
    n = n-1
    if n <= 0:
        print('n!=', result)
        break
