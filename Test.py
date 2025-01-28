class FreakyRhys():
    def __init__(self):
        self.freak = 100

class FreakyAaron(FreakyRhys):
    def __init__(self):
        super().__init__()

test = FreakyRhys()
print(test)