# 1 1~n까지의 2의 배수의 합
sum = 0
n = int(input('n:'))
i = 0
while i <= n:
    if i % 2 == 0:
        sum = sum+i
    i += 1
print('0~', n, '까지의 2의 배수의 합:', sum)
