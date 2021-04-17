from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

print(f'Logging In... with username: {username}, password: {password}')