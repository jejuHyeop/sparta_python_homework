import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from modules.utils import valid_input, intro, paint_screen
from random import randint as ri

intro_ment = """안녕하세요. 가위~ 바위~ 보~ 게임입니다.
5 초 안에 안내면 무조건 패!!
나머지 룰은 말안해도 아실거에요 ~
입력은 각각 가위는 1, 바위는 2, 보는 3 으로 입력해주세요!!
종료를 원한다면 언제든 q 를 입력해주세요.
게임을 시작해볼까요?"""
intro(intro_ment, 0.01, [2,4])

# 승, 패, 드로
score = [0, 0, 0]
choices = ['가위','바위','보']

def judge(ch):
    judge_string = "1231"
    if ch in judge_string:
        return False
    return True

while True:
    paint_screen()
    computer_input = ri(1,3)
    user_index = valid_input("가위(1) 바위(2) 보(3) > ", range(1,4), int, 5)

    if user_index:
        ch = str(user_index) + str(computer_input)

        print(f"당신은 {choices[user_index-1]}, 컴퓨터는 {choices[computer_input-1]} 을 냈네요!!")

        # 비기는 경우
        if computer_input == user_index:
            print("DRAW I:")
            score[2] += 1
        else:
            if judge(ch):
                print("YOU WIN :)") 
                score[0] += 1
            else:
                print("YOU LOSE >:")
                score[1] += 1
    else:
        print("YOU LOSE >:")
        print("\n\nTIME IS GOLD!!")
    
    input("\n\n[ENTER]")
    paint_screen()
    
    retry_input = valid_input('한판더 하실건가요 y/n > ', ['y','n'], str).lower()
    if retry_input == 'n':
        print("=" * 30)
        for st, num in zip(['승','패','무'], score):
            print(f"{st} : {num} 회")
        print("=" * 30)
        break
    
    
