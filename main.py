import inputnumber
from inputnumber import request_number


def print_hi(name, value):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}. you have entered {value}')  # Press Ctrl+F8 to toggle the breakpoint.

def tobasis(number:int, basis:int):

    result = ""
    neva = False
    if number < 0:
        neva = True
        number = -number
    digits = "0123456789abcdef"

    if number == 0:
        result = "0"

    while number != 0:
        reminder = number % basis
        number = number // basis
        result += digits[reminder]

    if neva:
        result += "-"
    return (result[::-1])






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    v = request_number()
    print_hi('Liana', v)



    for r in range(2, 17):

        print(f"this number under basis ({r}): ", tobasis(v, r))
















