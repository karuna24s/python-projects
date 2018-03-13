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
    # What this method would do is allows us to see Post.from_mongo and give us an id and it will give
    # us back the Mongo data that we get from that database.
    @staticmethod
    def from_mongo(id):
        # this method will find one post that has a specific id
        # Post.from_mongo('123')
        return Database.DATABASE.find_one(collection='posts', query={'id': id})

    @staticmethod
    def from_blog(id):
        # this method will find all the posts that has a specific blog_id
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
