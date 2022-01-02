# Cracker Barrel Peg Game Solution Finder

I couldn't beat the Cracker Barrel peg game. So I wrote a Python script to do it for me.

Enter the inital empty peg position (sample board shows position indeces), and the program recursively tests every possible move
until a winning combination of moves is found. It is possible to win no matter which hole is left empty at the beginning of the game.

## Sample Usage
```
   ** solution finder for the Cracker Barrel peg game **

Board position indeces:

                       0
                     1   2
                   3   4   5
                 6   7   8   9
               10  11  12  13  14

Enter starting empty hole>> 0
Solution:
        peg 3 jumps peg 1
        peg 5 jumps peg 4
        peg 0 jumps peg 2
        peg 6 jumps peg 3
        peg 9 jumps peg 5
        peg 11 jumps peg 7
        peg 12 jumps peg 8
        peg 1 jumps peg 4
        peg 2 jumps peg 5
        peg 14 jumps peg 9
        peg 5 jumps peg 8
        peg 13 jumps peg 12
        peg 10 jumps peg 11

   ** solution finder for the Cracker Barrel peg game **
```
