
from modules.h3_load_save import load_members
import hashlib

membersDict = load_members()

def sha256_hash(text):
    encoded_text = text.encode('utf-8')
    sha256 = hashlib.sha256()
    sha256.update(encoded_text)
    hashed_text = sha256.hexdigest()
    return hashed_text

def login():
    print("="*20 + " LOGIN " + "="*20)
    username = input("아이디를 입력해주세요 > ")
    password = input("패스워드를 입력해주세요 > ")
    for mem in membersDict:
        if mem.username == username and mem.password == sha256_hash(password):
            print()
            print(f"{username} 님 환영합니다!!")
            return mem
    print("아이디와 패스워드를 확인해주세요 :(")