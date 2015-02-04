#!/usr/bin/env python

from math import floor

func=lambda x: floor(2**(30.403243784-x**2))*10**-9

uList = []
uVal = -1
while not uVal in uList:
	uList.append(uVal)
	uVal = func( uVal )
print sum(uList[-2:])
