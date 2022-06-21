# Random password generator

import random

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*'

while True:
    length =int(input('password length: '))
    passes = int(input('how many passwords: '))
    for x in range(0, passes):
        password = ''
        for x in range(0, length):
            char = random.choice(chars)
            password = password + char
        print(password)




