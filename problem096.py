from subprocess import check_output
import os

# install the package 'sudoku' in your favorite linux-distro

DATAFILE = "problem096_sudoku.txt"
PRECANNED = "problem096_sudoku_precanned.txt"
# original	=>	precanned
# Grid 001	=>	% Grid 001
# 010020030	=>	.1..2..3.
with open(DATAFILE, 'r') as in_file:
    with open(PRECANNED, 'w') as out_file:
        for line in in_file.readlines():
            if line[:4] == "Grid":
                out_file.write("% " + line)
            else:
                out_file.write(line.replace("0", "."))

solutions = check_output(["sudoku", "-v", "-fcompact", PRECANNED])
solutions = solutions.decode().split('\n')
# the solutions are put sequential and look like
# > Solution to ...
# > % Grid 001
# > [9 lines of 9 digits]
firstlines = solutions[2::11]
total = sum(int(firstline[:3]) for firstline in firstlines)
print(total)
os.unlink(PRECANNED)
