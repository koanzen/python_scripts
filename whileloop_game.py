cmd = ''
started = False

while True:
    cmd = input('> ').lower()
    if cmd == 'help':
        print(f'''start - to start the car
stop - to stop the car
quit - to exit''')
    elif cmd == 'start':
        if not started:
            print('The car starts.')
            started = True
        else:
            print('The car is already started')
    elif cmd == 'stop':
        if started:
            print('The car stops')
            started = False
        else:
            print('The car is currently stopped')
    elif cmd == 'quit':
        print('Exited the game.')
        break
    else:
        print('Wrong command.')
