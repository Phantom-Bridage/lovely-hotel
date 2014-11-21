#coding: utf-8

class FormatCheckResult(object):
    def __init__(self, result, index, comment):
        self.__result = result
        if self.__result == False and index < 0:
            raise IndexError("index is negative value")
        self.__index = index
        self.__comment = comment

    def get_result(self):
        return self.__result

    def get_index(self):
        return self.__index

    def get_message(self):
        message = "Wrong format in [{index}]: {comment}".format(index=self.__index, comment=self.__comment)
        return message
