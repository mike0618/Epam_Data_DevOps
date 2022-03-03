from sys import argv


def task3():
    if len(argv) > 1:
        while True:
            users_word = input('Guess a word: ')
            if users_word in argv[1:]:
                print('Great job!')
                break
            print('Try again!')


if __name__ == '__main__':
    task3()
