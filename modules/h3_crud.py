from modules.h3_load_save import load_posts
from modules.h3_classes import Post
from modules.h3_load_save import save_posts
from time import sleep
from colorama import Fore, Back, Style

postsDict = load_posts()

def access_process(func):
    def wrapper(login_object):
        if login_object:
            return func(login_object)
        else:
            print("우선 인증이 필요합니다!\n\n")
    return wrapper

@access_process
def post_create(login_object):
    print("="*50)
    print(f"{login_object} 님! 게시글을 생성해주세요")
    print("="*50)
    title = input("글 제목을 입력해주세요 : ")
    content = input("글 내용을 입력해주세요 : ")
    postsDict.append( Post({"title":title, "content":content, "author":login_object.username}) )
    for num, i in enumerate(".\n.\n.\n.\n게시글이 등록되었습니다!!", 1):
        print(i, end="")
        sleep(0.5 / num)
        
def post_read():
    if get_posts():
        for p in get_posts():
            print("="*50)
            print(f"글 제목 {p.title}")
            print(Back.LIGHTBLACK_EX + Style.DIM + Fore.WHITE + f"작성자 {p.author}" + Style.RESET_ALL)
            print("="*50)
            print(p.content)
            print()
            print(f"post id {p.id}")
            print()
            print()

@access_process
def post_update(login_object):
    if get_posts():
        print("="*50)
        print(f"{login_object} 님! 수정할 post id 값을 입력해주세요")
        print("="*50)
        try:
            postid = int(input("POST ID 입력 > "))
            p = get_post(postid)
            if p:
                if p.author == login_object.username:
                    print("-"*30)
                    print("원래 내용")
                    print("-"*30)
                    print(f"글 제목 : {p.title}")
                    print(f"글 제목 : {p.content}")
                    print()
                    print()
                    mod_title = input(f"수정할 제목을 입력하세요 : ")
                    mod_content = input(f"수정할 내용을 입력하세요 : ")
                    p.title, p.content = mod_title, mod_content
                else:
                    print("수정 권한이 없습니다.")
        except ValueError:
            print("postid 는 정수입니다!")
        
@access_process
def post_delete(login_object):
    if get_posts():
        try:
            postid = int(input("수정할 post id 값을 입력해주세요 : "))
            p = get_post(postid)
            if p:
                if p.author == login_object.username:
                    postsDict.pop(postsDict.index(p))
                    print("게시글이 삭제되었습니다")
                else:
                    print("삭제 권한이 없습니다.")
        except ValueError:
            print("postid 는 정수입니다!")
        



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

def post_save():
    save_posts(postsDict)