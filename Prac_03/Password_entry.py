MINIMUM_LENGTH = 6

"""Get password of valid size from user and print asterisks"""
password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
while len(password) < MINIMUM_LENGTH:
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))

print('*' * len(password))
