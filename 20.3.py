
def issimple(number, simplenumbs):
    for num in simplenumbs:
        if number % num == 0:
            return False
        if number // num < num:
            break
    return True


def logout(simplenumbs):
    for numb in simplenumbs:
        print(numb)


def intofile(simplenumbs, filename):
    with open(filename, "w") as f:
        for numb in simplenumbs:
            f.write(str(numb) + "\n")

def readfromfile(filename, numbersfromfile):
    with open(filename, "r") as p:
        for line in p:
            numbersfromfile.append(int(line.strip()))

if __name__ == '__main__':
    simplenumbs=[3, 5, 7, 11, 13]
    simplenumbs.append(17)
    for num in range(19, 100, 2):
        if issimple(num, simplenumbs):
            simplenumbs.append(num)
    logout(simplenumbs)
    myfilename = "C:\\Users\\Liana\\Desktop\\nmbss.txt"
    intofile(simplenumbs, myfilename)
    test = []
    readfromfile(myfilename, test)
    if test == simplenumbs:
        print("good read")
    else:
        print("bad read")


