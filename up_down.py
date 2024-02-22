from random import randint as ri
from utils import valid_input
from os import system
from time import sleep

intro_ment = """안녕하세요. 업그레이드 버전의 업다운 게임입니다.
랜덤한 숫자를 맞춰주시면 됩니다 ~
종료를 원한다면 언제든 q 를 입력해주세요.
게임을 시작해볼까요?"""

for st in intro_ment:
    print(st, end="")
    sleep(0.01)

input("\n\n게임시작 [ENTER]")
system("clear")


while True:
    system("clear")
    level_ment = """==============================
1. EASY (한 자리수)
2. NORMAL (두 자리수)
3. HARD (세 자리수)
==============================
난이도를 선택해주세요 > """
    level = valid_input(level_ment, ["1","2","3"], str)
    level = int(level)
    
    system("clear")
    try_time = 0
    msg = """
{} 번만에 맞췄습니다.

패널티 입력 > {} 회
일반적인 입력 > {} 회
"""
    boundary_min, boundary_max = 10 ** (level-1) , 10 ** level - 1
    panalty_min, panalty_max = boundary_min, boundary_max
    random_number = ri(boundary_min, boundary_max)
    panalty = 0

    while True:
        # 사용자가 3 초안에 입력하지 않을 경우 TimeoutOccurred Error 가 발생
        user_input = valid_input('숫자를 맞춰보세요 > ',range(boundary_min, boundary_max + 1), int, 10)
        
        if user_input:
            try_time += 1
            # 바운더리 체크 (바보 숫자 외칠경우 패널티 + 2)
            if panalty_min <= user_input <= panalty_max:
                if user_input > random_number:
                    print("DOWN!")
                    panalty_max = user_input - 1
                elif random_number > user_input:
                    print("UP!")
                    panalty_min = user_input + 1
                else:
                    system("clear")
                    print("CORRECT!")
                    print(msg.format(try_time, panalty, try_time - 2*panalty))
                    input("\n\nGAME CLEAR [ENTER]")
                    break
            else:
                print(f"{panalty_min} 에서 {panalty_max} 까지만 입력해주세요!")
                print("유효하지 않는 범위 입력으로 인해 패널티 발생!!")
                try_time += 1 # 패널티 발생!!
                panalty += 1 # 마지막 출력 화면을 위한 기록 > panalty
        else:
            print("시도회수가 1 증가합니다 ~")
            try_time += 1

        input("\n\nTry Again [ENTER]")
        system("clear")
    
    system("clear")
    retry_input = valid_input('게임을 다시 시작하시겠습니까 y/n > ', ['y','n'], str)
    if retry_input == 'n':
        break



