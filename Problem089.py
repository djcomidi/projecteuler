#!/usr/bin/env python

ROMANS = [ 'I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM',  'M' ]
VALUES = [   1,    4,   5,    9,  10,   40,  50,   90, 100,  400, 500,  900, 1000 ]

def roman_to_western(roman):
	western, idx = 0, 0
	while idx < len(roman):
		if roman[idx:idx+2] in ROMANS: d = 2
		else: d = 1
		t = ROMANS.index(roman[idx:idx+d])
		western += VALUES[t]
		idx += d
	return western

def western_to_roman(western):
	roman = ""
	while western > 0:
		n = max( filter( lambda v: v <= western, VALUES ) )
		roman += ROMANS[VALUES.index(n)]
		western -= n
	return roman

romans = []
with open('Problem089_roman.txt') as in_file:
	romans = [ line.strip() for line in in_file.readlines() ]

savings = 0
for roman in romans:
	western = roman_to_western(roman)
	romanshort = western_to_roman(western)
	savings += len(roman) - len(romanshort)
#	print "%5d %-16s %-16s" % ( western, roman, romanshort )

print savings
