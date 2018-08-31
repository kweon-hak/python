# exam004.py
# 10000 미만의 피나치오 수열 리스트로 만들기

# 피보나치 수는 0과 1로 시작하며,
# 다음 피보나치 수는 바로 앞의 두 피보나치 수의 합이 된다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

a=0
b=1
fibonacci = [a,b]

while True:
    c=a+b
    if c >= 100000:
        break;
    fibonacci.append(c)
    a,b = b,c


print(fibonacci)

