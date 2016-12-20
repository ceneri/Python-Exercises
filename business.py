#Cesar Neri
#December 19, 2016

#Excercise 16-1 from Murach's Python Programming Book

#Defines 3 classes to work with task manager



#!/usr/bin/env python3

class Task():

    def __init__(self, description, status = False):
        self.__status = status
        self.__description = description

    @property
    def status(self):
        return self.__status

    @property
    def description(self):
        return self.__description

    def toggleStatus(self):
        self.__status = not self.__status

    def __str__(self):
        string = self.__description

        if (self.__status) :
            string += " (COMPLETED)"
        else :
            string += " (INCOMPLETE)"

        return string


class TaskList():
    
    def __init__(self, name):
        self.__tasks = []
        self.__name = name
        self.__qty = 0

    @property
    def name(self):
        return self.__name

    @property
    def qty(self):
        return self.__qty

    def addTask(self, task):
        self.__tasks.append(task)
        self.__qty += 1

    def delTask(self, index):
        self.__tasks.pop(index)
        self.__qty -= 1

    def toggleTask(self, index):
        task = self.__tasks[index]
        task.toggleStatus()

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__tasks) - 1:
            raise StopIteration
        else:
            self.__index += 1
            return self.__tasks[self.__index]

    def __str__(self):
        string = self.__name.upper() + ":\n"
        i = 1
        for task in self:
            string += str(i) + ". " + str(task) + "\n"
            i += 1

        return string
        

class TaskManager():

    def __init__(self):
        self.__lists = []
        self.__count = 0

    @property
    def count(self):
        return self.__count

    def addList(self, tList):
        self.__lists.append(tList)
        self.__count += 1

    def delList(self, index):
        self.__lists.pop(index)
        self.__count -= 1

    def getList(self, index):
        return self.__lists[index]

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index == len(self.__lists) - 1:
            raise StopIteration
        else:
            self.__index += 1
            return self.__lists[self.__index]

    def __str__(self):
        string = ""
        for tList in self:
            string += str(tList) + "\n"

        return string
        
    
        
        
