# exam005.py

# 입력으로 주어진 수의 약수를 모두 구하기
# 일반적인 방법과 고속검색 방법을 비교

import math

def runtime(original_function):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print('{} 함수 총 실행시간: {} 초'.format(original_function.__name__, t2))
        return result

    return wrapper


# 일반적인 방법 사용
@runtime
def solution1(n):
    result = []
    for i in range(1,n+1) :
        if n%i == 0:
            result.append(i)
    return result

# 고속 검색기법 사용
@runtime
def solution2(n):
    temp_low = []
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i == 0:
            temp_low.append(i)

    # 나머지 약수를 구함
    result = []
    result.extend(temp_low)
    for i in temp_low:
        result.append(int(n/i))

    result = list(set(result)) # 중복제거
    result.sort() # 정렬
    return result

num = input("숫자를 입력하세요: ")

print(solution1(int(num)))
print(solution2(int(num)))


