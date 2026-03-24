
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


def intofile(simplenumbs, filnam):
    with open(filnam, "w") as f:
        for numb in simplenumbs:
            f.write(str(numb) + "\n")


if __name__ == '__main__':
    simplenumbs=[3, 5, 7, 11, 13]
    simplenumbs.append(17)
    for num in range(19, 100, 2):
        if issimple(num, simplenumbs):
            simplenumbs.append(num)
    logout(simplenumbs)
    intofile(simplenumbs, "C:\\Users\\Liana\\Desktop\\nmbss.txt")





