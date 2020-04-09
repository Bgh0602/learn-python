# 입력 n에 대한 n! 출력

n = int(input('n:'))
result = 1
origin = n
while True:
    n = n*(origin-result)
    result = result+1
    if (origin-result) <= 0:
        print('n!=', n)
        break
