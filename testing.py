import random

def gen_pass():
    letters = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
               'C', 'V', 'B', 'N', 'M', 'q', 'w', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j',
               'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', "="]

    pass_list = []
    test = (random.choice(letters) for _ in range(3))
    # pass_list.append(random.choice(numbers) for _ in range(1))
    # pass_list.append(random.choice(symbols) for _ in range(5))
    # print(pass_list)

gen_pass()
