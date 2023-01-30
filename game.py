hearts = "Hearts"
diamonds = "Diamonds"
clubs = "Clubs"
spades = "Spades"

# list comprehension
rankList = [x for x in range(1, 14)]


class deck():
    def __init__(self, Suit, Rank, Name):
        self.Suit = Suit
        self.Rank = Rank
        self.Name = Name


# test = deck()


# listObjectDeck = [deck(),deck(),deck()]
listOfHearts = []
acehearts = deck(hearts, 11, "ACE")
towHearts = deck(hearts, 2, "TWO")
threeHearts = deck(hearts, 3, "THREE")
fourHearts = deck(hearts, 4, "FOUR")
fiveHearts = deck(hearts, 5, "FIVE")


acehearts.Name
print(towHearts.Rank)
