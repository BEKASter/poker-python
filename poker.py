import random

class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def show_card(self):
		return [self.value, self.suit]


class Deck:
	def __init__(self):
		create_deck()
		mix()

	def mix(self):
		for i in range(5):
			for j in range(52):
				new_poz = random.randint(52)
				k = self.cards[new_poz]
				self.cards[new_poz] = self.cards[j]
				self.cards[j] = k

	def give_card(self):
		return self.cards.pop()

	def create_deck(self):
		self.cards = []
		for value in 'A123456789JQK':
			for suit in 'DHSC':
				if (value == '1'):
					value = '10'
				self.cards.append(Card(value, suit))


class Table:
	def __init__(self):
		self.cards = []
		self.chips = 0

	def get_card(self, card):
		self.cards.append(card)

	def get_chips(self, chips):
		self.chips += chips

	def give_chips(self, chips):
		self.chips -= chips
		return chips

	def show_cards(self):
		return self.cards


class Player:
	def __init__(self, chips):
		self.cards = []
		self.chips = chips

	def make_a_bet(self, chips):
		if (chips <= self.chips):
			self.chips -= chips
			return chips
		else:
			c = self.chips
			self.chips = 0
			return c

	def get_chips(self, chips):
		self.chips += chips

	def get_card(self, card):
		self.cards.append(card)

	def show_cards(self):
		return self.cards

	def show_chips(self):
		return self.chips


class Game:
	def __init__(self, num_players, num_chips):
		self.players = []
		for i in range(num_players):
			self.players.append(Player(num_chips))
		
