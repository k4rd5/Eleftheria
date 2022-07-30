from system.main_menu import *
from system.inventory_options import inventory_options
from engine.util import clear, status
from engine.game import Game


save_path = "saves//"


def gamestart():
    running = True
    while running:
        clear()
        choice = title_options()
        clear()
        if choice == 'e':
            running = False
        elif choice == 'l':
            file_ = load_game(save_path).split('.')[0]
            clear()
            if not file_:
                continue
            else:
                blank = Game('blank')
                blank.load(file_)
                print('would you like to continue with the following save file?')
                blank.player.information()
                choice = input('continue?> ').lower().strip()
                if choice == 'y':
                    game = blank
                    main_loop(game)
                else:
                    continue
        elif choice == 'n':
            info = new_game()
            game = Game(info[0])
            game.save(info[1])
            main_loop(game)
        else:
            continue


def movement(choice, game):

    if choice == "w":
        game.location.move(2)
    elif choice == "s":
        game.location.move(3)
    elif choice == "a":
        game.location.move(0)
    elif choice == "d":
        game.location.move(1)


def main_loop(game):
    running = True
    game.clock.tick()
    env_list = game.data.environments
    markers = {env_name[0].capitalize(
    ): env_name for env_name in env_list.keys()}
    clear()
    while running:
        clear()
        status(game, env_list)
        game.location.display(list(markers.keys()))
        print("\n[w] [a] [s] [d]")
        print('[e] save and exit')
        print('[i] inventory')
        print('[p] player information')
        choice = input("> ").lower().strip()
        clear()
        if choice in 'wasd':
            game.clock.tick()
            movement(choice, game)
        elif choice == 'e':
            # start from here
            file_ = load_game(save_path).split('.')[0]
            game.save(file_)
            break
        elif choice == 'i':
            inventory_options(game)
        current_env = game.location.generate_choice(list(env_list.values()))

        game.player.enter(current_env())


gamestart()
