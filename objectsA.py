#Cesar Neri
#December 18, 2016

#Author objects

#Use of the __iter__(), __str(), and __next__()


#!/usr/bin/env python3


class Book:
    def __init__(self, title="", authors=None):
        self.title = title
        self.authors = authors

    def getDescription(self):
        return self.title + " by " + self.authors

    def __str__(self):
        return self.title + " by " + str(self.authors)
                
class Author:
    def __init__(self, firstName="", lastName=""):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        return self.firstName + " " + self.lastName

class Authors:
    def __init__(self):
        self.__list = []

    def add(self, author):
        self.__list.append(author)

    @property
    def count(self):
        return len(self.__list)

    def __str__(self):
        string = ""
        for i in range(self.count):
            string += str(self.__list[i]) + ", "

        return string[:-2]

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__list) - 1:
            raise StopIteration
        else:
            self.__index += 1
            return self.__list[self.__index]
