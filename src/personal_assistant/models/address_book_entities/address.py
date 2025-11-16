class HomeAddress:
    def __init__(self, *args):
        """Initialize HomeAddress with a variable number of string arguments."""
        self.value = " ".join(args)

    def __str__(self):
        return self.value
