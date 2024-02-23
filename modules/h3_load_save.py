import csv
from .h3_classes import Post, Member

membersDict, postsDict = [], []
# CSV 파일 열기
def load_members():
    members_file = "data/members.csv"
    with open(members_file, newline='') as csvfile:
        members = csv.DictReader(csvfile)
        for mem in members:
            membersDict.append(Member(mem))
    return membersDict
    
def load_posts():
    posts_file = "data/posts.csv"
    with open(posts_file, newline='') as csvfile:
        posts = csv.DictReader(csvfile)
        for post in posts:
            postsDict.append(Post(post))
    return postsDict

def save_posts(savedicts):
    posts_file = "data/posts.csv"

    with open(posts_file, 'w', newline='') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=['id','title','content','author'])
        csv_writer.writeheader()
        for sd in savedicts:
            csv_writer.writerows([{'id':sd.id, 'title':sd.title, 'content':sd.content, 'author':sd.author}])
    