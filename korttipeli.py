#!/usr/bin/python3

import random
from stack import Stack
from exceptions import *


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

    def __repr__(self):
        return 'Player({}, RFG_pile={})'.format(self.name, self.RFG_pile)

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
        return self.hand.pop(index).pop()

    def flipCardInHand(self, index):
        self.hand[index].peek().visible = not self.peekCardFromHand(index).visible



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

        to_be_returned += '\n'

        for x in range(len(self.cards)):
            temp = ''
            for y in range(len(self.cards[x])):
                if str(self.getCard(x, y)) != "None":
                    temp += str(self.getCard(x, y))
                else:
                    temp += "<>"
                temp += ' '
            to_be_returned += temp
            to_be_returned += '\n'


        to_be_returned += '\nAmount of cards in the deck: ' + str(self.deck.amount_of_cards)

        return to_be_returned

    def deal(self, player_template, table_template):

        # käsikortit
        for player in self.players:
            for i in player_template:
                temp_stack = Stack()
                for a in i.stack:
                    real_card = self.deck.drawCard()
                    real_card.visible = a.visible
                    temp_stack.push(real_card)
                player.addCardToHand(temp_stack)

        # pöytäkortit
        for x in range(len(table_template)):
            for y in range(len(table_template[x])):
                for card in table_template[x][y].stack:
                    real_card = self.deck.drawCard()
                    real_card.visible = card.visible
                    self.cards[x][y].push(real_card)


        return None


    def getCard(self, x, y):
        # if x > self.size_x or y > self.size_y:
        #     return "from Function getCard: 'x > self.size_x or y > self.size_y' = True"
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

    def takeCardFromTable(self, x, y):
        return self.cards[x][y].pop()


class Cell(object):
    object_count = 0

    def __init__(self, *args):
        self.stack = args
        self.__id = Cell.object_count  # So that the Python memory management doesn't get too excited about merging two same-looking objects :)
        Cell.object_count += 1

    def __str__(self):
        return 'type:<Cell>; ' + str(self.stack)

    @property
    def how_many_stacked(self):
        return len(self.stack)

#
# käsi = []
# for i in range(4):
#     käsi.append(Cell(Card(visible=False)))
#
# pöytä = [[]]
# for i in range(4):
#     pöytä[0].append(Cell(Card(visible=True)))
#
#
# deck = DeckOfCards(52)
# deck.shuffle()
#
# players = [Player('kaappo'), Player('kaappo2')]
#
# pelipöytä = Table(4, 1, players, deck)
#
#
# pelipöytä.deal(käsi, pöytä)
#
# pelipöytä.takeCardFromTable(0, 2)
# print(pelipöytä)
