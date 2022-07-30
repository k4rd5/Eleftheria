from os import listdir, path
from datetime import datetime


def title_options():
    print('The EleftheriaRPG Project')
    print('(name subject to change)')
    print('-'*40)
    print('[N] New Game')
    print('[L] Load Game')
    print('[E] Exit')

    return input('> ').lower().strip()


def new_game():
    pass


def load_game(save_path):
    print('Save files')
    print('[0] exit')
    save_files = []
    for file_ in listdir(save_path):
        if file_.endswith('.sav'):
            save_files.append(file_)

    for n, file_ in enumerate(save_files):
        mtime = path.getmtime(save_path+file_)
        print(
            f'[{n+1}] {file_} {datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")}')
    choice = int(input('> '))
    if choice <= 0:
        return False
    else:
        return save_files[choice-1]


def initialize_game(filename):
    pass


# add more stuff here later
def new_game():
    name = input('Enter your name: ')
    choice = input('continue?> ').lower().strip()
    if choice == 'y':
        save = input('enter save name:')
        return [name, save]  # weird pls change
    else:
        return False
