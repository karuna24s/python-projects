class Post(object):
    # init methods stands for initialize and is the method that gets called when
    # when you say you want to create a new thing called a post and this thing
    # is going to have the following content and title
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
