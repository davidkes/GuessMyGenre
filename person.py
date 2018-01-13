"""
Program: person.py

This creates a person's class with attributes name, age,  and origin
"""

class Person(object):

    def __init__(self):
        self.name = ''
        self.age = 0
        self.origin = ''

    def getName(self):
        """returns the name of a person"""
        return self.name

    def getAge(self):
        """returns the age of a person"""
        return self.age

    def getOrigin(self):
        """returns the origin of a person"""
        return self.origin

    def setName(self, name):
        """sets a person's name"""
        self.name = name

    def setAge(self, age):
        """sets a person's age"""
        self.age = age

    def setOrigin(self,origin):
        """sets where a person is from"""
        self.origin=origin