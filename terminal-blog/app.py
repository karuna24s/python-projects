import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

# students = collection.find({})
# student_list = []

# list comprehension: when you do a for loop it is because you want to do something with each of the
# elements of the list that you are iterating over.
# create a student list variable. The append method gets the empty student list variable and then
# adds something to it, so each of the students in our student collection would be going into the
# student list and then we would end up with student list being our list of students.
# for student in students:
#     student_list.append(student)

# Let's say we don't want to do that: Let's say we want to say that our students are the students in
# this collection. Put this collection.find inside a pair of square brackets and then we would say
# the contents of this student's list is each of the student for student in students. But students
# is really collection.find. So what we are saying here is for each of the elements in this collection.find
# which we are calling student, simply put all of it inside this new list and what this does is if we print
# students, it puts all the students inside a list.

students = [student for student in collection.find({})]
# print out mark
# students = [student['mark'] for student in collection.find({})]
print(students)
