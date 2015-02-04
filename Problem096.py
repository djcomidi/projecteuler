#!/usr/bin/env python

# install the package 'sudoku' in your favorite linux-distro

from EulerTools import execute_command

DATAFILE = "Problem096_sudoku.txt"
PRECANNED = "Problem096_sudoku_precanned.txt"
# original	=>	precanned
# Grid 001	=>	% Grid 001
# 010020030	=>	.1..2..3.
with open(DATAFILE,'rb') as in_file:
	with open(PRECANNED,'wb') as out_file:
		for line in in_file.readlines():
			if line[:4] == "Grid":
				out_file.write("% "+line)
			else:
				out_file.write(line.replace('0','.'))

solutions = execute_command("sudoku","-v -fcompact "+PRECANNED)
solutions = solutions.split('\n')
# the solutions are put sequential and look like
# > Solution to ...
# > % Grid 001
# > [9 lines of 9 digits]
firstlines = solutions[2::11]
print sum( int(firstline[:3]) for firstline in firstlines )
