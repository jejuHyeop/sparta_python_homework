from inputimeout import inputimeout, TimeoutOccurred

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