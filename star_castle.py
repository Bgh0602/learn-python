# n을 입력하면 n층의 별성을 출력
n = int(input('n:'))
floor = 1
star = '*'
while n > 0:
    n = n-1
    print(floor*star)
    floor += 1
