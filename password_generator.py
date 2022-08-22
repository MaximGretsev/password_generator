import secrets
import string


def main():
    """Documentation about main function"""
    pass_length = length_of_password()
    gen = generator_of_password(pass_length)
    print(f"Your password: {gen}")


def length_of_password():
    length = int(input("Length of password: "))
    return length


def generator_of_password(length):
    options_for_pass = string.digits + string.ascii_letters + string.ascii_uppercase + string.punctuation
    generate_pass = ''.join(secrets.choice(options_for_pass) for _ in range(length))
    return generate_pass


if __name__ == '__main__':
    main()
