#!/usr/bin/env python

RANKS = "__23456789TJQKA"
TYPES = ["","RoyalFlush","StraightFlush","FourOfAKind","FullHouse",
		"Flush", "Straight", "ThreeOfAKind", "TwoPair", "OnePair", "HighCard" ]

def filter_repetition( ranks, repetition ):
	return [ rank for rank in set(ranks) if ranks.count(rank) == repetition ]

def value_of_hand(hand):
	ranks = sorted( [ RANKS.index(card[0]) for card in hand ], reverse=True ) # high -> low
	suits = sorted( [ card[1] for card in hand ] ) # A -> Z
	is_straight = all([ max(ranks)-ranks[i]==i for i in xrange(5) ])
	is_flush = len(set(suits)) == 1
	rankcounts = [ ranks.count(r) for r in set(ranks) ]
	if is_straight and is_flush and max(ranks) == 14:
		return 10, 14 # Royal flush
	if is_straight and is_flush:
		return 9, max(ranks) # Straight flush
	if 4 in rankcounts:
		return 8, filter_repetition(ranks,4)[0] # Four of a kind
	if 3 in rankcounts and 2 in rankcounts:
		return 7, filter_repetition(ranks,3)[0] # Full house
	if is_flush:
		return 6, max(ranks) # Flush
	if is_straight:
		return 5, ranks # Straight
	if 3 in rankcounts:
		return 4, filter_repetition(ranks,3)[0] # Three of a kind
	if rankcounts.count(2) == 2:
		return 3, max( filter_repetition(ranks,2) ) # Two pair
	if rankcounts.count(2) == 1:
		return 2, filter_repetition(ranks,2)[0] # One pair
	return 1, max(ranks) # Highest card

winsPlayerA = 0
with open('Problem054_poker.txt','r') as in_file:
	for line in in_file.readlines():
		handsAB = line[:-2].split(' ')
		typeA, highA = value_of_hand(handsAB[:5])
		typeB, highB = value_of_hand(handsAB[5:])
		if typeA > typeB or ( typeA == typeB and highA > highB ):
			winsPlayerA += 1
print winsPlayerA
