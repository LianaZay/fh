import os
from os import listdir
from os.path import isfile, isdir,  join

def countfiles(path):
    amo = 0
    for f in listdir(path):
        fullname = join(path, f)
        if isfile(fullname):
            amo = amo + 1
        else:
            try:
                if f != ".." and f != "." and isdir(fullname):
                    if os.access(fullname, os.R_OK):
                        amo = amo + countfiles(fullname)
            except PermissionError:
                print("folder name is inaccessible: ", fullname)
    return amo


if __name__ == '__main__':
    print("Liana")
    result = countfiles("C:\\")

    print("result is ", result)

