#!/usr/bin/python3
"""module with class MyInt that inherits from int."""
class MyInt(int):
     """int operators == and !=."""
    def __eq__(self, other):
        return self - other != 0

    def __ne__(self, other):
        return self - other == 0
