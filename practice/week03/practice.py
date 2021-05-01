# 주석
# js : console.log('test')
print('test')

# let, const 없음
number = 1
float_number = 1.1  # js에서는 일반적으로 floatNumber
string = '문자열'
boolean = True  # js에서는 true

# list, dict 거의 똑같음
number_list = [1, 2, 3, 4]
string_dict = {'name': 'Kim', 'age': 30}
print(string_dict['name'])

# python의 특징
# 들여쓰기가 아주 중요함
if number > 10:
    print('10보다 큽니다.')
else:
    print('10보다 작습니다.')

for num in number_list:
    print(num)


def func(num):
    print(num)


def sum(num1, num2):
    result = num1 + num2
    return result


print(sum(10, 20))

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '배', '수박']
count = 0
for fruit in fruits:
    if fruit == '사과':
        count += 1
print(count)
