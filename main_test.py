# 문제 설명
# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

# 제한 사항
# n은 1,000,000 이하의 자연수 입니다.

# 입출력 예
# n	result
# 78	83
# 15	23
# 입출력 예 설명
# 입출력 예#1
# 문제 예시와 같습니다.
# 입출력 예#2
# 15(1111)의 다음 큰 숫자는 23(10111)입니다.

# def solution(n):
#     answer = n
#     # print(answer)
#     return answer

# def change(num):
#     binary=""
#     while num !=0:
#         if num%2==0:
#             binary="0"+binary
#             num=num//2
#         else:
#             binary="1"+binary
#             num=num//2
#     return binary

# a= 1%2
# print(f'a= {a}')


# print(change(10))



# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.


# input 받고 for loop 돌리고 
# 그 돌린문자 받고 length(text)해서 for loop 돌림
# 문자를 arraylist에 넣고 (array 와 arraylist의 차이점) 연속되는 단어 찾기 하기 처음단어가 a 면 지역변수에 text[].add 이렇게 해서 넣어놓고 돌리다가 if 분기 나눠서 add 돌리고 된거 다르면 add하고 돌리고 만약에 (if) text[] 부분에 index[i] i는 추가할때 i++ 해놓음
# 그 문자랑 다르면 그륩단어 아님


# import sys

# num_string = int(input())
# strings = []


# for i in range(num_string):
#     string = input()
#     strings.append(string)

# for string in strings:
#     print(string)



# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# import sys
# num = int(input())

# if (num%2) == 0:
#     print ('Even')
# else:
#     print('Odd')

# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# def solution(arr):

#     answer = 0
#     for i in range(arr.length()):
#         answer = answer + arr[i]
#         return answer


#TODO 아직 못품
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
# def solution(n):
#     a = []
#     n = str(n)
#     answer = 0
#     for i in range(len(n)):
#         a.append(int(n[i]))
#     for j in range(len(a)):
#         answer = answer + a[j]
#     return answer 



# 나머지가 없는 문제
# arr = [5,9,7,10]
# divisor = 5

# def solution(arr, divisor):
#     print(f'arr: {arr}')
#     answer = []
#     for i in range (len(arr)):
#         # answer에 하나라도 값이 들어왔다는 가정하
#         if len(answer) > 1:
#             # 나머지가 없을때
#             if arr[i]%divisor == False:
#                 answer.append(arr[i])
#                 print(f'if answer: {answer}')
#         # 값이 하나도 없을때
#         else:
#             if arr[i]%divisor == False:
#                 answer.append(arr[i])
#                 print(f'else answer: {answer}')
#     answer.sort()
#     if len(answer) == 0:
#         answer.append(-1)
#     return answer    

# result = solution(arr,divisor)
# print (result)


# https://school.programmers.co.kr/learn/courses/30/lessons/12910



# 문제 설명
# 자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 답이 항상 존재함은 증명될 수 있습니다.

# def solution(n):
#     answer = 0
#     i = 0
#     while True:
#         i = i + 1
#         if n%i == 1: 
#             answer = i
#             return answer


# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
# https://school.programmers.co.kr/learn/courses/30/lessons/12950

# def solution(arr1, arr2):
#     answer = []
#     for i in range (len(arr1)):
#         answer.append([])
#         for j in range (len(arr1[i])):
#             answer[i].append(arr1[i][j] + arr2[i][j])
#     return answer

# arr3 = []
# arr1 = [[1,2],[3,4]]
# arr2 = [[5,6],[7,8]]
# print(arr1[0][0] + arr1[1][1])
# print(len(arr1))
# arr3.append([])
# arr3[0].append(arr1[0][0] + arr2[0][0])

# print (arr3)



# https://school.programmers.co.kr/learn/courses/30/lessons/135808

# for loop으로 score의 len을 modm로 하고 몫만 남김.
# sort된 부분에서 마지막 값 -1 값이 k 가 아니라면, 첫번째 값 * m을 함 그 값을 a = a+x 이런식으로 저장함
# 마지막 loop 다돌면 해당 값 리턴


# def solution(k, m, score):
#     score = []
#     answer = 0
#     qu = len(score)//m
#     score.sort()
#     arr = []
#     for i in range(qu): #몫(qu)가 3이면 3번 돈다
#         for j in range(m): #1번째 몫일때 k
#             arr.append(score[j]) #[1, 2, 3, 1, 2, 3, 1] 라면 sort되니 [1,1,1,2,2,3,3] 이렇게 되고
#             score.pop(0) #[1,1,2,2,3,3] 이렇게 하나가 빠지고 arr = [1] 이렇게 됨
#             if arr[0] != k:
#                 answer += arr[0]*m
#             else:
#                 answer += k*m
#     return answer

k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]


# 이거 반대로 되어야됨. 지금은 sort해서 112233 이런식인데 그게 아니라 33222이런식으로 쌓여서,
# 거기에서 제일 마지막값 * 상자에 담긴 사과 개수 * 상자 개수 이렇게 되야됨
# 그래서 arr.append(score.pop(0)) 이부분이 pop(-1)이런식으로 제일 뒤에꺼 하던지 sort를 뒤부터 하던지 해야될듯
# k = 최상품 사과 점수
# m = 사과 상자에 담기는 개수

# def solution(k, m, score):
#     answer = 0
#     qu = len(score)//m
#     print(f'qu = {qu}')
#     score.sort()
#     arr = []
#     for i in range(qu):
#         print(f'i = {i}')
#         for j in range(m): 
#             print(f'j = {j}')
#             arr.append(score.pop(-1))
#             print(f'arr2 = {arr}')
#             print(f'score2 = {score}')
#         arr.sort()
#         answer += arr[0]*m
#         print(f'arr[0]!=k {answer}')
#         # if 
#         #     answer += k*m
#         #     print(f'arr[0]=k {answer}')
#     return answer

# def solution(k, m, score):
#     score_count = [0]



# # answer = 4/3
# # print(int(answer))


# def solution2(k, m, score):
#     score.sort(reverse=True)
#     print(score)
#     print(len(score))
#     answer = 0
#     for i in range(0, len(score)-m+1, m):
#         min_in_box = min(score[i:i+m])
#         print(f'{i}번째 : {min_in_box}') 
#         answer += min_in_box * m
#         print(answer)
#     return answer

# print(solution2(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))


# absolutes =  [4,7,12]
# signs = ['true','false','true']

# def solution(absolutes, signs):
#     answer = 0
#     for i in range(len(absolutes)):
#         if signs[i] == 'true':
#             answer = answer + absolutes[i]
#             print(f'true : {answer}')
#         if signs[i] == 'false':
#             answer = answer - absolutes[i]
#             print(f'false : {answer}')
#         print(f'return : {answer}')
#     return answer

# print(solution(absolutes, signs))


# 4/16-1/17
# 약수의 개수와덧셈
# 풀이시간 1시간
# def solution(left, right):
#     answer = 0
#     for i in range((right-left)+1):
#         factor = 0
#         for j in range(left+i):
#             if ((left+i)%(j+1) == 0):
#                 print(f'left+i: {left+i}')
#                 print(f'j+1: {j+1}')
#                 factor += 1
#                 print(f'factor ==0: {factor}')
#         print(f'left: {left+i}')
#         print(f'factor: {factor}')
#         if (factor%2 !=0):
#             answer -= (left+i)
#         if (factor%2 ==0):   
#             answer += (left+i)
#     return answer


# 스택과 큐에 관련된 문제
# 같은숫자는 싫어
# 4/17 
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if (arr[i-1] != arr[i]):
            answer.append(arr[i])
    return answer


# 숫자 문자열과 영단어 - kakao 채용연계형 인턴쉽
# 4/17
def solution(s):
    answer = 0
    return answer