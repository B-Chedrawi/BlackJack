import random


values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7,
          'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,  'Queen': 10, 'King': 10, 'Ace': 11}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


three_of_clubs = Card("Clubs", "Three")
two_hearts = Card("Hearts", "Two")

# print(two_hearts)
# print(two_hearts.value)
# print(two_hearts.suit)
# print(values[two_hearts.rank])

print(two_hearts.value < three_of_clubs.value)


class Deck:

    def __init__(self):

        self.all_cards = []  # empty list with no input from the user

        for suit in suits:
            for rank in ranks:
                # Create the Carrd Object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

        random.shuffle(self.all_cards)


new_deck = Deck()

# print(len(new_deck.all_cards)) check the length


# print(new_deck.all_cards[1])

# for card_object in new_deck.all_cards:
# print(card_object)
