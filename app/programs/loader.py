from collections import namedtuple
import os

Program = namedtuple("Program", "title location")

def load(directory):
    files = os.listdir(directory)
    files.remove('__init__.py')

    base = directory.replace("/", ".") + "."

    list = {}
    for file in files:
        name = file[0:-3]
        title = name.replace("_", " ")
        list[name] = Program(title, base + name)

    return list
