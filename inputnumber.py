
def is_digit(danamba):
    return danamba == '0' \
        or danamba == '1' \
        or danamba == '2' \
        or danamba == '3' \
        or danamba == '4' \
        or danamba == '5' \
        or danamba == '6' \
        or danamba == '7' \
        or danamba == '8' \
        or danamba == '9'

def request_number():
    number = ""
    while len(number) < 1:
        number = input("number from -100000000 to 100000000: ")
        neva = False
        if len(number) > 0:
            if number[0] == '-':
                neva = True
                number = number[1:]
            elif number[0] == '+':
                number = number[1:]
        if len(number) < 1:
            continue
        for n in number:
            if not is_digit(n):
                number = ""
                break
        if len(number) < 1:
            continue

        intv = int(number)
        if intv > 100000000 or intv < -1000000000:
            continue
        if neva: inv = -inv
        return intv

