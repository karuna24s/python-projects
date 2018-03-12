# Create a database class for database interactions. This class that I am creating
# is an object with properties and methods on top of what a database can do.
# Since our database is an object with extra properties and methods, it will also
# be able to do everything that the object can do. So when we define more methods
# we will have all the object methods as well as the database methods we define
# (this is called Inheritance) We are getting our database class to inherit from
# this object and that way our entries will contain all of those methods that the
# object has in place.
# Don't need an init method because we don't want to create multiple instances
# of an object. We want all of our connections to go to one URI and want one database.
# We need the same database for this project. We only need the post and blog connections.
# @staticmethod means we are not going to use self in a method because this method
# belongs only to the database class as a whole and never to an instance of a database.

import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        # Give the insert method a collection, get that collection and insert the data.
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)
