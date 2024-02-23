
class Member:
    def __init__(self, kwargs):
        self.name = kwargs['name']
        self.username = kwargs['username']
        self.password = kwargs['password']
    
    def display(self):
        print(f"회원 명 : {self.name}")
        print(f"회원 닉네임 : {self.username}")
    
    def __repr__(self):
        return self.username

class Post:
    post_id = 1

    def __init__(self, kwargs):
        self.id = Post.post_id
        self.title = kwargs['title']
        self.content = kwargs['content']
        self.author = kwargs['author']
        Post.post_id += 1
