
class Member:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.username = kwargs['username']
        self.password = kwargs['password']

    def display(self):
        print("="*30)
        print("정보 보기")
        print("="*30)
        print(f"이름 > {self.name}")
        print(f"아이디 > {self.username}")
    
    def __repr__(self):
        return self.username

class Post:
    post_id = 1

    def __init__(self, **kwargs):
        self.id = Post.post_id
        self.title = kwargs['title']
        self.content = kwargs['content']
        self.author = kwargs['author']
        Post.post_id += 1
    
    
