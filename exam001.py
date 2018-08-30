# exam001.py
# 자연수 자릿수 더하기

""""
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는
solution 함수 만들기
N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
"""

# 일반적인 알고리즘으로 풀이
def solution(num):
    sum = 0
    while num > 0:
        sum += num % 10 # 첫째 자리수를 구하여 더함
        num = int(num / 10)  # 첫째 자리수를 제거
    return sum

# python type으로
def solution_python(num):
    str_num = str(num)
    sum = 0
    for i in str_num:
        sum += int(i)
    return sum


num = 12345678910
print(solution(num))
print(solution_python(num))