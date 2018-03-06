#!/usr/bin/python3

import random
from stack import Stack


class DrawCardError(Exception):
    pass


class DealingError(Exception):
    pass


class Card(object):
    def __init__(self, suit=None, value=None, visible=False):
        self.suit = suit
        self.value = value
        self.visible = visible

    def __str__(self):
        visual_representation_closed = {'diamonds': '♢', 'clubs': '♧', 'spades': '♤', 'hearts': '♡'}
        visual_representation_open = {'diamonds': '♦', 'clubs': '♣', 'spades': '♠', 'hearts': '♥'}

        if None in [self.suit, self.value]:
            return 'Undef'
        special_values = {**{11: 'J', 12: 'Q', 13: 'K', 14: 'A'}, **{x: x for x in range(11)}}
        if self.visible:
            return '{} {}'.format(visual_representation_open[self.suit], special_values[self.value])
        else:
            return '{} {}'.format(visual_representation_closed[self.suit], special_values[self.value])
        return ''


    def __repr__(self):
        return 'Card({}, {}, {})'.format(self.suit, self.value, self.visible)


class DeckOfCards(object):
    suits = ['clubs', 'spades', 'hearts', 'diamonds']

    def __init__(self, amount_of_cards, ace_as_one=False):
        self.ace_as_one = ace_as_one
        self.__cards = []

        for suit in DeckOfCards.suits:
            if ace_as_one:
                for value in range(1, 14):
                    self.__cards.append(Card(suit, value))
            else:
                for value in range(2, 15):
                    self.__cards.append(Card(suit, value))

    def shuffle(self):
        for i in range(len(self.__cards) - 1, 0, -1):
            random_index = random.randint(0, i - 1)
            self.__cards[random_index], self.__cards[i] = self.__cards[i], self.__cards[random_index]

    def drawCard(self):
        if self.amount_of_cards == 0:
            print("hei")
            raise DrawCardError("Can't drawCard() from an empty stack!")

        temp = self.__cards.pop()
        return temp

    @property
    def amount_of_cards(self):
        return len(self.__cards)

    def __repr__(self):
        return 'DeckOfCards({}, ace_as_one={})'.format(self.amount_of_cards, self.ace_as_one)


class Player(object):
    def __init__(self, name, RFG_pile=None):
        self.hand = []
        self.name = name
        self.RFG_pile = RFG_pile
        if RFG_pile is not None:
            self.RFG_pile = []

    @property
    def amount_of_cards(self):
        return len(self.hand)

    def __str__(self):
        to_be_returned = ''

        to_be_returned += self.name + ': '

        temp = []
        for i in self.hand:
            # print(i.peek())
            temp.append(str(i.peek()))

        to_be_returned += ', '.join(temp)
        return to_be_returned

    def addCardToHand(self, stack):
        self.hand.append(stack)

    def peekCardFromHand(self, index):
        return self.hand[index].peek()

    def drawCardFromHand(self, index):
        return self.hand[i].pop(index).pop()

    def flipCardInHand(self, index):
        self.hand[index].peek().visible = not self.peekCardFromHand(index).visible

    def __repr__(self):
        return 'Player({}, RFG_pile={})'.format(self.name, self.RFG_pile)


class Table(object):
    def __init__(self, size_x, size_y, players, deck):
        self.size_x = size_x
        self.size_y = size_y
        self.players = players
        self.deck = deck
        self.cards = []
        for y in range(size_y):
            temp = []
            for x in range(size_x):
                temp.append(Stack())
            self.cards.append(temp)

    def __str__(self):
        to_be_returned = ''
        for i in self.players:
            to_be_returned += str(i)
            to_be_returned += '\n'

        to_be_returned += '\nAmount of cards in the deck: ' + str(self.deck.amount_of_cards)

        return to_be_returned

    def deal(self, player_template, table_template):
        for player in self.players:
            for i in player_template:
                temp_stack = Stack()
                for a in i.stack:
                    real_card = self.deck.drawCard()
                    real_card.visible = a.visible
                    temp_stack.push(real_card)
                player.addCardToHand(temp_stack)
        print(self.deck.amount_of_cards)
        for y in range(len(table_template)):
            for x in range(len(table_template[y]) - 1):
                temp_stack = Stack()
                for a in table_template[x][y]:
                    real_card = self.deck.drawCard()
                    print(real_card)
                    real_card.visible = a.visible
                    temp_stack.push(real_card)
                try:
                    # self.cards[x][y] = temp_stack
                    self.setCard(x, y, temp_stack)
                except:
                    raise DealingError('The table_template is different size than the size of the table!')
        return None

        # for y in range(len(table_template)):
        #     for x in range(len(y)):
        #         temp_stack = Stack()
        #         real_card = self.deck.drawCard()
        #         real_card.
        #         self.cards[x][y] = self.deck.drawCard()
        #         self.cards[x][y].visible = x.visible

    def getCard(self, x, y):
        if x >= self.size_x or y >= self.size_y:
            return None
        return self.cards[x][y]

    def setCard(self, x, y, value):
        if x >= self.size_x or y >= self.size_y:
            return None
        self.cards[x][y] = value
        return None

    def giveCard(self, giver, receiver, index):
        receiver.hand.append(giver.drawCardFromHand(index))
        return None

    def putCardToTable(self, x, y, player, index):
        self.cards[x][y].push(player.drawCardFromHand(index))
        return None

    def flipCard(self, x, y):
        self.getCard(x, y).visible = not self.getCard(x, y).visible


class Cell(object):
    object_count = 0

    def __init__(self, *args):
        self.stack = args
        self.__id = Cell.object_count  # So that the Python memory management doesn't get too excited about merging two same-looking objects :)
        Cell.object_count += 1

    def __str__(self):
        return 'type:<Cell>; ' + str(self.stack.peek())

    @property
    def how_many_stacked(self):
        return len(self.stack)


bismarkin_käsi = []

for i in range(10):
    bismarkin_käsi.append(Cell(Card(visible=False), Card(visible=True)))
for i in range(6):
    bismarkin_käsi.append(Cell(Card(visible=False)))

bismarkin_pöytä_template = []
# for i in range(10):
#     bismarkin_pöytä_template.append([Cell(Card(visible=False), Card(visible=True))])


deck = DeckOfCards(52)
deck.shuffle()

players = [Player('kaappo'), Player('kaappo2')]

bismarkin_pöytä = Table(2, 10, players, deck)
bismarkin_pöytä.deal(bismarkin_käsi, [])

# for i in players:
#     print(i)

print(bismarkin_pöytä)

players[0].flipCardInHand(2)
print(bismarkin_pöytä)
