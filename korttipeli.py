#!/usr/bin/python3

import random
from stack import Stack


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


class DeckOfCards(object):
    suits = ['clubs', 'spades', 'hearts', 'diamonds']

    def __init__(self, amount_of_cards, ace_as_one=False):
        self.ace_as_one = ace_as_one
        self.cards = []

        for suit in DeckOfCards.suits:
            if ace_as_one:
                for value in range(1, 14):
                    self.cards.append(Card(suit, value))
            else:
                for value in range(2, 15):
                    self.cards.append(Card(suit, value))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            random_index = random.randint(0, i - 1)
            self.cards[random_index], self.cards[i] = self.cards[i], self.cards[random_index]

    def drawCard(self):
        temp = self.cards.pop()
        return temp

    @property
    def amount_of_cards(self):
        return len(self.cards)


class Player(object):
    def __init__(self, name, RFG_pile=False):
        self.hand = []
        self.name = name
        self.RFG_pile = RFG_pile
        if RFG_pile:
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


class Table(object):
    def __init__(self, size_x, size_y, players, deck):
        self.size_x = size_x
        self.size_y = size_y
        self.cards = [[Card() for i in range(size_x)] for i in range(size_y)]
        self.players = players
        self.deck = deck

    def __str__(self):
        to_be_returned = ''
        for i in self.players:
            to_be_returned += str(i)
            to_be_returned += '\n\n'

        to_be_returned += '\n\n\nAmount of cards in the deck: ' + str(self.deck.amount_of_cards)

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


        for y in table_template:
            for x in y:
                self.cards[x][y] = self.deck.drawCard()
                self.cards[x][y].visible = x.visible



class Cell(object):
    def __init__(self, id, *args):
        self.stack = args

    def __str__(self):
        return 'type:<Cell>; ' + str(self.stack.peek())

    @property
    def how_many_stacked(self):
        return len(self.stack)


bismarkin_käsi = []

for i in range(10):
    bismarkin_käsi.append(Cell(i, Card(visible=False), Card(visible=True)))
for i in range(6):
    bismarkin_käsi.append(Cell(i, Card(visible=False)))


deck = DeckOfCards(52)
deck.shuffle()

players = [Player('kaappo'), Player('kaappo2')]

bismarkin_pöytä = Table(0, 0, players, deck)
bismarkin_pöytä.deal(bismarkin_käsi, [])

# for i in players:
#     print(i)

print(bismarkin_pöytä)
