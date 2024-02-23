from modules.utils import valid_input, paint_screen
from modules.h3_login import login
from modules.h3_crud import post_create, post_read, post_update, post_delete, post_save

from colorama import Fore, Style, Back
import colorama

colorama.init()


login_status = False

if __name__ == "__main__":
    
    user_ment = """================================================
포스트 관리 시스템
================================================
1. 로그아웃
2. 게시글 생성
3. 게시글 조회
4. 게시글 수정
5. 게시글 삭제
6. 프로그램 종료

메뉴 입력 > """

    anon_ment = """================================================
포스트 관리 시스템
================================================
1. 로그인
2. 게시글 생성
3. 게시글 조회
4. 게시글 수정
5. 게시글 삭제
6. 프로그램 종료

메뉴 입력 > """

    login_ment = ""
    login_object = None
    while True:
        paint_screen()
        if login_object:
            print(Fore.BLUE + Back.CYAN + Style.BRIGHT + f"현재 {login_object} 님 로그인 중!" + Style.RESET_ALL)
            user_choice = valid_input(user_ment, ['1','2','3','4','5','6'], str)
        else:
            print(Fore.BLUE + Back.LIGHTYELLOW_EX + Style.BRIGHT + f"당신은 익명의 사용자입니다." + Style.RESET_ALL)
            user_choice = valid_input(anon_ment, ['1','2','3','4','5','6'], str)
        
        paint_screen()
        if user_choice == '1':
            if login_object:
                login_object = None
                print("로그아웃 되었습니다!")
            else:
                login_object = login()

        elif user_choice == '2':
            post_create(login_object)

        elif user_choice == '3':
            post_read()

        elif user_choice == '4':
            post_update(login_object)

        elif user_choice == "5":
            post_delete(login_object)
        else:
            post_save()
            break
        input("\n\n\n메뉴로 돌아가기 [ENTER]")
    