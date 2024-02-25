from modules.h3_post_module import author_find
from modules.h3_load_save import load_members, save_mems
from modules.h3_classes import Member
import hashlib

membersDict = load_members()

def sha512_hash(text):
    encoded_text = text.encode('utf-8')
    sha512 = hashlib.sha512()
    sha512.update(encoded_text)
    hashed_text = sha512.hexdigest()
    return hashed_text

def login():
    print("="*20 + " LOGIN " + "="*20)
    username = input("아이디를 입력해주세요 > ")
    password = input("패스워드를 입력해주세요 > ")
    for mem in membersDict:
        if mem.username == username and mem.password == sha512_hash(password):
            print()
            print(f"{username} 님 환영합니다!!")
            return mem
    print("아이디와 패스워드를 확인해주세요 :(")

def valid_check(username):
    for mem in membersDict:
        if username == mem.username:
            return False
    return True

def member_create():
    name = input("이름을 입력해주세요 > ")
    while True:
        username = input("아이디를 입력해주세요 > ")
        if not valid_check(username):
            print("아이디가 중복되었습니다!")
        elif not username.isalnum():
            print("아이디는 영어, 숫자 조합입니다!")
        else:
            break
    password = sha512_hash(input("패스워드를 입력해주세요 > "))
    member = Member(username=username, name=name, password=password)
    membersDict.append(member)
    

def member_read(login_object):
    login_object.display()
    print()
    print("="*30)
    print(f"{login_object.username} 님이 작성한 게시글")
    print("="*30)
    author_find(login_object.username)
    


def member_save():
    save_mems(membersDict)