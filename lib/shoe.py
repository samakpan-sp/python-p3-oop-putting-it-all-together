class Shoe:
    CATEGORY = ["Nike", "Vasace", "v3", "Louis Vuitton", "Sports"]

    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        if value not in Shoe.CATEGORY:
            print(f"Error: '{value}' is not a valid category. Choose from {Shoe.CATEGORY}")
        else:
            self._name = value

    name = property(get_name, set_name)

black = Shoe("Nike")
print(black.name)

c = Shoe("Sports")
c.name = "Louis Vuitton"
print(c.name)


