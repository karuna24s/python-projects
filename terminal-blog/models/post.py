from database import Database


class Post(object):
    # init methods stands for initialize and is the method that gets called when
    # when you say you want to create a new thing called a post and this thing
    # is going to have the following content and title
    def __init__(self, blog_id, title, content, author, date, id):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self.id = id

    # add a method to save the post to the database
    # connect to the database and it will insert some data in this collection (posts)
    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    # creates a JSON representation of the post itself. This JSON representation
    # is just key: value set
    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }
