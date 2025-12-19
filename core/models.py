from mongoengine import Document, StringField, IntField, ReferenceField

class Course(Document):
    name = StringField(required=True)
    duration = StringField()

    meta = {"collection": "courses"}

    def __str__(self):
        return self.name


class Student(Document):
    name = StringField(required=True)
    age = IntField()
    course = ReferenceField(Course)

    meta = {"collection": "students"}

    def __str__(self):
        return self.name
