
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


if __name__ == '__main__':
    simplenumbs=[3, 5, 7, 11, 13]
    simplenumbs.append(17)
    for num in range(19, 100000000, 2):
        if issimple(num, simplenumbs):
            simplenumbs.append(num)
    logout(simplenumbs)





