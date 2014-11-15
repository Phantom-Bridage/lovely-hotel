# coding: utf-8
class Converter:
    @classmethod
    def to_str(self, sql_data):
        lst = []
        for i, it in enumerate(map(str, sql_data)):
            lst.append(it)
        return lst
