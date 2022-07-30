# inventory.py - revised 17/9/21

from .item_system import Stack


class Inventory:
    def __init__(self, items=[], currency={}):
        self.items = items
        self.currency = {
            "gold": 0,
            "silver": 0,
            "copper": 0,
            "nugget": 0,
            "gem": 0,
        }

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        for stack in self.items:
            yield stack

    def check_item(self, item, amount=1):
        if type(item) is str:
            item = self.get_item_object(item.strip().lower())
        if item:
            amount_ = self.item_amounts(item)
            if amount_ and amount_[item] >= amount:
                return True
        return False

    def check_currency(self, currency, reqAmount=0):
        if currency in self.currency.keys():
            if self.currency[currency] >= reqAmount:
                return True
        return False

    @property
    def item_list(self) -> list:
        items = {}
        for stack in self.items:
            items[stack.item] = None
        return list(items.keys())

    @property
    def total_items(self) -> int:
        return len(self.item_list)

    @property
    def total_stacks(self) -> int:
        return len(self)

    def clear(self):
        self.items = []
        self.currency = {}

    def get_item_object(self, name=None):
        for stack in self.items:
            if name.strip().lower() == stack.name.lower():
                return stack.item
        return False

    def get_stack(self, item):
        for stack in self.items:
            if item.name == stack.name:
                return stack
        return False

    def item_amounts(self, item=None) -> dict:
        results = {}
        for stack in self.items:
            if item and stack.item is not item:
                continue
            elif stack.item not in results.keys():
                results[stack.item] = 0
            results[stack.item] += stack.amount
        return results

    def stack_amounts(self):
        return [{stack.name: stack.amount} for stack in self.items]

    def add_item(self, item, amount=1):
        remainder = amount
        for stack in self.items:
            if stack.item.name == item.name:
                if stack.isfull:
                    continue
                else:
                    remainder = stack.add(amount)
        if remainder:
            remainder = self.create_stack(item, remainder)

        if remainder:
            self.add_item(item, remainder)

    def remove_item(self, item, amount=1):
        remainder = amount
        for stack in self.items[::-1]:
            if stack.item.name == item.name:
                remainder = stack.remove(remainder)
                if remainder or stack.amount == 0:
                    self.items.remove(stack)

        return remainder

    def take_item(self, item, amount=1):
        remainder = self.remove_item(item, amount)
        return (item, amount - remainder)

    def create_stack(self, item, amount=1):
        new = Stack(item, 0)
        self.items.append(new)
        return new.add(amount)

    def use_item(self, item, victim):
        stack = self.get_stack(item)
        if not stack:
            return False
        if stack.number_of_uses > 0:
            stack.number_of_uses -= 1
        else:
            return False
        item.use(victim)
        if stack.number_of_uses <= 0:
            stack.amount -= 1
            if stack.isempty:
                self.items.remove(stack)
            else:
                stack.number_of_uses = item.number_of_uses

    # currency

    def give_currency(self, currency, amount):
        if self.check_currency(currency):
            self.currency[currency] += amount
        else:
            self.currency[currency] = amount

    def take_currency(self, currency, amount):
        if self.check_currency(currency, amount):
            self.currency[currency] -= amount
        else:
            return False


class Currency:
    VALUES = {
        "gold": 500,
        "silver": 100,
        "copper": 20,
        "nugget": 1,
        "gem": 921,
    }


class Bank(Inventory):
    def __init__(self, items=[], currency={}):
        super().__init__(items, currency)

    def currency_convert(self, from_, to):
        # from is a tuple with previous currency name and amount
        return (to, (from_[1] / (Currency.VALUES[to] / Currency.VALUES[from_[0]])))

    # i dont have a better name
    def convert_everything_to(self, to):
        new = {to: 0}
        for currency, amount in self.currency.items():
            converted = self.currencyConvert((currency, amount), to)[1]
            new[to] += converted
        self.currency = new
