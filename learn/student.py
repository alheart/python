#!/bin/python

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return "Student object (name: %s)" % self.name

    __repr__=__str__
    
    def print_score(self):
        print("%s: %s" % (self.name, self.score))

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart
lisa
bart.print_score()
lisa.print_score()
