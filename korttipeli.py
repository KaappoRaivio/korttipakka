#!/usr/bin/python3

import random


class Card(object):
    def __init__(self, suit=None, value=None, visible=False):
        self.suit = suit
        self.value = value
        self.visible = visible

    def __str__(self):
        visual_representation_closed = {'diamonds': '♢', 'clubs': '♧', 'spades': '♤', 'hearts': '♡'}
        visual_representation_open = {'diamonds': '♦', 'clubs': '♣', 'spades': '♠', 'hearts': '♥'}

        special_values = {**{11: 'J', 12: 'Q', 13: 'K', 14: 'A'}, **{x: x for x in range(11)}}
        if self.visible:
            return '{} {}'.format(visual_representation_open[self.suit], special_values[self.value])
        else:
            return '{} {}'.format(visual_representation_closed[self.suit], special_values[self.value])


class DeckOfCards(object):
    suits = ['clubs', 'spades', 'hearts', 'diamonds']

    def __init__(self, amount_of_cards, ace_as_one=False):
        self.ace_as_one = ace_as_one
        self.amount_of_cards = amount_of_cards
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
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.hand = []
        self.name = name

    def __setattr__(self, name, value):
        if name == 'hand':
            super(Player, self).__setattr__(name, value)
            super(Player, self).__setattr__('amount_of_cards', len(self.hand))
        else:
            super(Player, self).__setattr__(name, value)


    def __str__(self):
        temp = []
        for i in self.hand:
            temp.append(str(i))
        return ', '.join(temp)

    def addCardToHand(self, suit, value, visible):
        self.hand = self.hand + [Card(suit, value, visible)]


class Table(object):
    def __init__(self, size_x, size_y, players, deck):
        self.size_x = size_x
        self.size_y = size_y
        self.players = players
        self.deck = deck

    def deal(self, template):
        for player in self.players:
            for template in template.cards_to_players:
                card = self.deck.drawCard()
                player.addCardToHand(card.suit, card.value, template.visible)


class DealTemplate(object):
    def __init__(self, cards_to_table, cards_to_players):
        self.cards_to_table = cards_to_table
        self.cards_to_players = cards_to_players



bismarkin_käsi = [Card(visible=True) for i in range(10)] + [Card(visible=False) for i in range(6)]


deck = DeckOfCards(52)
deck.shuffle()

template = DealTemplate([], bismarkin_käsi)

kaappo = Player('kaappo')

table = Table(1, 1, [kaappo], deck)

table.deal(template)
print(kaappo)
