# 윤년(leaf year)
'''
1. 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않음
2. 400으로 나누어 떨어짐
'''
# 윤년 판단하기
print('enter year')
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('leaf year')
else:
    print('common year')
