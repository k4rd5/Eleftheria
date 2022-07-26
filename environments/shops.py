from engine.environment import Environment


class Shop(Environment):
    def __init__(self, items=None, type_=None):
        self.owner = 'Jeff'
        self.type = type_ or 'miscellanous'
        self.items = items or []

    # the interface for letting a player sell items
    def sell(self, player, item, amount=1):
        pass

    def multiply_cost(self, n, cost):
        for currency, amount in cost.items():
            cost[currency] = amount*n
        return cost

    def on_entry(self, player):
        self.inside = True
        print(f"Welcome to {self.owner}'s {self.type} shop!")
        n = 0
        for itemname, item in self.items.items():
            print(f'{n+1}. {itemname} - {item.cost}')
            n += 1
        print('[e] exit')
        choice = input('Enter Choice: ').strip().lower()
        if choice == 'e':
            self.on_exit()
        else:
            choice = int(choice)
            amount = int(input('Enter Amount: '))
            item = list(self.items.values())[choice-1]
            final_cost = self.multiply_cost(amount, item.cost)
            print(
                f'Would you like to buy "{item.name}" x{amount} for {final_cost}')
            if not input('> ').lower().strip() in ['y', 'yes']:
                self.on_entry(player)
            else:
                if player.take_currencies(final_cost):
                    player.add_item(item, amount)
                    print('Transaction was successful.')
                    print(f'BALANCE:{player.inventory.currency}')
                else:
                    print('Not enough funds for transaction')
                self.on_entry(player)

    def on_exit(self):
        self.inside = False
