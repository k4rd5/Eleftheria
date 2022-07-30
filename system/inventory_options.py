def inventory_options(game):
    print('Inventory Items:')
    print('-'*30)
    print(game.player.inventory.stack_amounts())
