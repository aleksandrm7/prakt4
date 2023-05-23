import random

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

def print_random_number_2():
    random_number_2 = random.randint(1, 200)
    print(random_number_2)

print_random_number_2()