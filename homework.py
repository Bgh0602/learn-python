# 9
import random
num = int(input('숫자를 입력하세요: '))
while num < 1:
    print('다시!')
    num = int(input('숫자를 입력하세요: '))

num2 = random.randint(1, num)
print('1~', num, '까지의 무작위 값은', num2, '이다.')

# 10
sum = 0
count = 1
print('0~100 까지의 숫자를 입력하세요.')
max = -1
min = 101
while True:
    a = input()
    if a == '입력끝':
        break
    a = int(a)
    if a > 100 or a < 0:
        print('error')
        break
    if a > max:
        max = a
    if a < min:
        min = a
    sum = sum+a
    count += 1

print('sum:', sum, '', 'average:', sum/(count-1))
print('max:', max, '', 'min:', '', min)
