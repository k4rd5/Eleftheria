# FILLERS


class FillerItem:
    def __init__(self, param, item=None, type_=str, optional=False):
        self.param = param  # parameter in output data
        self.value = item
        self.type = type_
        self.optional = optional

    def __call__(self):
        return self.value


class FillerQuantity(FillerItem):
    def __init__(self, param, quantity=None):
        super().__init__(param, quantity, int)


# CONSTANTS


class Constant(FillerItem):
    def __init__(self, value, type_, optional=False):
        super().__init__(None, value, type_, optional)


class StringConstant(Constant):
    def __init__(self, value):
        super().__init__(value, str)


class IntegerConstant(Constant):
    def __init__(self, value):
        super().__init__(value, int)


fillers = [FillerItem, FillerQuantity]
constants = [Constant, StringConstant, IntegerConstant]


def sanitizedInput(text, chars='~`!@#$%^&*()-=+[]{{}}|\\<>.?/:;"'):
    input_ = input(text).lower().strip()

    for char in chars:
        input_ = input_.replace(char, "")
    words = input_.split(" ")

    s_words = []
    for word in words:
        if word != "":
            try:
                s_words.append(int(word.strip()))
            except:
                s_words.append(word.strip())
    return s_words


def parseCommand(format_, command):
    if len(command) > len(format_) or len(format_) > len(command):
        return False
    data = {}
    for i, argument in enumerate(format_):
        if type(argument) in constants:
            if argument.value != command[i]:
                return False
        elif type(argument) in fillers:
            if type(command[i]) == argument.type:
                data[argument.param] = command[i]
            else:
                return False
    return {"cmd": command[0], "data": data}


def run(func, data):
    return func(**data["data"])


if __name__ == "__main__":

    remove_cmd_format = [
        StringConstant("remove"),
        FillerItem("item"),
        FillerQuantity("quantity"),
    ]
    use_cmd_format = [
        StringConstant("use"),
        FillerItem("item"),
    ]
    choose_option_1 = [IntegerConstant(1)]

    cmd_formats = {
        "remove": remove_cmd_format,
        "use": use_cmd_format,
        "1": choose_option_1,
    }

    inventory_cmd = sanitizedInput("> ")

    for cmd, cmd_format in cmd_formats.items():
        data = parseCommand(cmd_format, inventory_cmd)
        if data:
            print(data)
