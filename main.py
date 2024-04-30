import random

print('Welcome to Password Gnerator\n')

passwAmount = int(input('Enter the amount of passwords needed: '))
passwLength = int(input('Enter the length of passwords: '))

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,/1234567890!@#$%^&*()'

print('\nHere are your passwords:')

for pwd in range(passwAmount):
    passwords = ''
    for c in range(passwLength):
        passwords += random.choice(char)
    print(passwords)

