import random

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    print_hi('PyCharm')

def print_random_number():
    random_number = random.randint(1, 100)
    print(random_number)

print_random_number()