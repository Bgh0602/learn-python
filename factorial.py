# 입력 n에 대한 n! 출력

n = int(input('n:'))
result = 1
while n > 1:
    result = result*n
    n = n-1
    print('n!=', result)
