#python
from inputimeout import inputimeout, TimeoutOccurred
from time import sleep
from os import system
from colorama import Fore, Style
import colorama
from .run_os import get_os

colorama.init()
def intro(st, time, line=[]):
    system("clear")
    cnt = 1
    for ch in st:
        if line:
            if ch == "\n":
                cnt += 1
            if cnt in line:
                print(Fore.RED, end="")
            else:
                print(Style.RESET_ALL, end="")
        print(ch, end="")
        sleep(time)
    input("\n\n게임시작 [ENTER]")


def valid_input(st, boundary, return_type, time=None):
    while True:
        if time == None:
            user_input = input(st).strip()
        else:
            try:
                user_input = inputimeout(prompt=st, timeout=time).strip()
            except TimeoutOccurred:
                print("입력 시간 초과!!")
                return None   
        if user_input == 'q':
            print("프로그램 강제 종료 !!")
            exit(1) 
        if return_type == int:
            try:
                if "." in user_input:
                    print("정수만 입력해주세요!!")
                else:
                    user_input = int(user_input)
            except:
                print("숫자만 입력해주세요!!")
        if user_input in boundary:
            return user_input
        print("입력값이 유효하지 않습니다!!")
        input("\n\nRETRY [ENTER]")
        system("clear")

def paint_screen():
    if get_os() == "windows":
        system("cls")
    else:
        system("clear")