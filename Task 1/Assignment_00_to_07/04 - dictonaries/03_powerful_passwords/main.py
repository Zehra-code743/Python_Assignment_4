from hashlib import sha256

def hash_password(password):
    return sha256(password.encode('utf-8')).hexdigest

def login(email, password ,stored_logins):

    return stored_logins.get(email) == hash_password(password)


def main():
    stored_logins = {
        'qZDlD@example.com': 'password1',
        'example@example.com': 'password2',
        'test@example.com': 'password3',
        'admin@example.com': 'password4'
    }

    email = input('Enter your email: ')
    password = input('Enter your password: ')

    if login(email, password, stored_logins):
        print('Login successful')
    else:
        print('Login failed')

        if __name__ == "__main__":
            main()