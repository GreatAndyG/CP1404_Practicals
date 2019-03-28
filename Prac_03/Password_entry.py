MINIMUM_LENGTH = 6


def main():
    """Get password of valid size from user and print asterisks"""
    print_password()


def print_password():
    password = get_password()
    print('*' * len(password))


def get_password():
    password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of at least {} characters: ".format(MINIMUM_LENGTH))
    return password


main()
