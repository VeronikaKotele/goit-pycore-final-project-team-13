class HomeAddress:
    def __init__(self, **args):
        try:
            # todo: validate address format
            self.value = " ".join(args.values())
        except ValueError:
            raise ValueError("Invalid format for address.")

    def __str__(self):
        return self.value
