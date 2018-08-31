# exam003.py
# 1000 보다 작은 자연수 중에 3 또는 5의 배수를 모두 더하라

sum = 0
for i in range(1,1000):
    if i%3 ==0 or i%5==0:
       sum +=i

print("sum:%d"%sum)
