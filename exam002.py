# 숫자 야구게임
import random

# 게임을 위한 랜덤 숫자 생성
# 1-9 사이의 숫자 3개 생성
rn = random.sample(range(1,10),3)
#print(rn)

t_cnt = 0   # 시도 횟수
s_cnt = 0   # 스트라이크 갯수
b_cnt = 0   # 볼 갯수

# 사용자 입력을 받음
print("숫자 야구게임을 시작합니다.")
print("-------------------------")

while(s_cnt < 3):
    user_input = str(input("3자리 숫자를 입력하세요: "))
    s_cnt = 0
    b_cnt = 0

    for i in range(0,3):
        for j in range(0,3):
            if(user_input[i] == str(rn[j]) and i == j):
                s_cnt +=1
            elif(user_input[i] == str(rn[j]) and i != j):
                b_cnt +=1

    print("{0} strike, {1} ball".format(s_cnt,b_cnt))
    t_cnt +=1

print("-------------------------")
print("빙고!!!")
print("{0} 번 만에 정답을 맞추었습니다.".format(t_cnt))