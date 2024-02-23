from utils import valid_input
from os import system
import hashlib
from colorama import Fore, Style
import colorama
from classes import Post, Member
from member_post_loadsave import load_members, load_posts, save_posts

colorama.init()
def sha256_hash(text):
    encoded_text = text.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(encoded_text)
    hashed_text = sha256.hexdigest()
    return hashed_text

login_status = False

def login():
    global login_object
    print("="*10 + " LOGIN " + "="*10)
    username = input("INPUT USERNAME > ")
    password = input("INPUT PASSWORD > ")
    for mem in membersDict:
        print(mem, sha256_hash(password))
        if mem.username == username and mem.password == sha256_hash(password):
            print("login success")
            login_object = mem
        
def logout():
    global login_object
    login_object = None
    
def access_process(func):
    def wrapper():
        global login_object
        if login_object:
            func()
        else:
            print("우선 인증이 필요합니다!\n\n")
            login()
            if not login_object:
                print("CHECK USERNAME or PASSWORD!!")
    return wrapper

@access_process
def post_create():
    title = input("글 제목을 입력해주세요 : ")
    content = input("글 내용을 입력해주세요 : ")
    postsDict.append( Post(title=title, content=content, author=login_object) )

def post_read():
    if get_posts():
        for p in get_posts():
            print("="*50)
            print(f"글 제목 {p.title}")
            print(f"작성자 {p.author}")
            print("="*50)
            print(p.content)
            print()
            print(f"post id {p.id}")
            print()
            print()

def get_post(postid):
    if postid:
        for p in postsDict:
            if p.id == postid:
                return p
        else:
            print("게시글이 존재하지 않습니다.")

def get_posts():
    if postsDict:
        return postsDict
    print("게시글이 존재하지 않습니다.")
    
@access_process
def post_update():
    if get_posts():
        try:
            postid = int(input("수정할 post id 값을 입력해주세요 : "))
            p = get_post(postid)
            if p.author == login_object.username:
                mod_title = input(f"{p.title} > 수정할 제목을 입력하세요 : ")
                mod_content = input(f"{p.content} > 수정할 내용을 입력하세요 : ")
                p.title, p.content = mod_title, mod_content
            else:
                print("수정 권한이 없습니다.")
        except:
            print("postid 는 정수입니다!")
        

@access_process
def post_delete():
    if get_posts():
        try:
            postid = int(input("수정할 post id 값을 입력해주세요 : "))
            p = get_post(postid)
            if p.author == login_object.username:
                postsDict.pop(postsDict.index(p))
                print("게시글이 삭제되었습니다")
            else:
                print("삭제 권한이 없습니다.")
        except:
            print("postid 는 정수입니다!")
        


    
if __name__ == "__main__":
    membersDict, postsDict = load_members(), load_posts()

    user_ment = """================================================
포스트 관리 시스템
================================================
1. 로그아웃
2. 게시글 생성
3. 게시글 조회
4. 게시글 수정
5. 게시글 삭제
6. 프로그램 종료
"""

    anon_ment = """================================================
포스트 관리 시스템
================================================
1. 로그인
2. 게시글 생성
3. 게시글 조회
4. 게시글 수정
5. 게시글 삭제
6. 프로그램 종료
"""

    login_ment = ""
    login_object = None
    while True:
        if login_object:
            print(Fore.BLUE + Style.DIM + f"현재 {login_object} 님 로그인 중!" + Style.RESET_ALL)
            user_choice = valid_input(user_ment, ['1','2','3','4','5','6'], str)
        else:
            print(Fore.BLUE + Style.DIM + f"당신은 익명의 사용자입니다." + Style.RESET_ALL)
            user_choice = valid_input(anon_ment, ['1','2','3','4','5','6'], str)
        
        if user_choice == '1':
            if login_object:
                logout()
            else:
                login()

        elif user_choice == '2':
            post_create()

        elif user_choice == '3':
            post_read()

        elif user_choice == '4':
            post_update()

        elif user_choice == "5":
            post_delete()
        else:
            print(postsDict)
            save_posts(postsDict)
            break


