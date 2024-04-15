# 텍스트 입력
# text1 = input()
# print(text1)

# 숫자 입력
num = int(input('숫자 주셈": '))
print(num)

# 여러개 값 입력
# st1, st2 = input('문자열 주셈: ').split()
# print(st1, st2)
# print(st1)
# print(st2)

#10951
# while True:
#     try:
#         nm1, nm2 = input().split()
#         if int(nm1) > 0:
#             nm1= int(nm1)
#         if int(nm2) < 10:
#             nm2= int(nm2)
#     except:
#         break
#     print(nm1+nm2)

#10807
# count = int(input())
# list_num = list(map(int,input().split()))
# v = int(input())
# print(list_num.count(v))


#8/20 코테 LV0 시작 하루 20문제씩 월~금 완료

# a, b = input().strip().split(' ')
# b = int(b)
# result = a * b
# print(result)


# str = input()
# result = ''

# for i in str:
#     if i.islower():
#         result += i.upper()
#     if i.isupper():
#         result += i.lower()

# print(result)

# print('!@#$%^&*(\'"<>?:;')

# a, b = map(int, input().strip().split(' '))
# print(f'{a} + {b} = {a + b}')


def solution(a, b, c):
    a = 2
    b = 6
    c = 1
    answer = 0
    if (a != b) or (b != c) or (a != c):
        answer = a + b + c
    if ((a == b) or (b == c) or (c == a)) and ((a != b) or (b != c) or (a != c)):
        answer = (a+b+c) + (a*a) + (b*b) + (c*c)
    if (a == b == c):
        answer = (a+b+c) + (a*a) + (b*b) + (c*c) + (a*a*a) + (b*b*b) + (c*c*c)
    return answer

