# Gess-Game

Gess is a chess variant. You can see the rules [here](https://www.chessvariants.com/crossover.dir/gess.html).  Note that when a piece's move causes it to overlap stones, any stones covered by the **footprint** get removed, not just those covered by one of the piece's stones.  It is not legal to make a move that leaves you without a ring.  It's possible for a player to have more than one ring.  A player doesn't lose until they have no remaining rings.

Locations on the board will be specified using columns labeled a-t and rows labeled 1-20, with row 1 being the Black side and row 20 the White side.  The actual board is only columns b-s and rows 2-19.  The center of the piece being moved must stay within those boundaries.  An edge of the piece may go into columns a or t, or rows 1 or 20, but any pieces there are removed at the end of the move.  Black goes first.

There's an online implementation [here](https://gess.h3mm3.com/) you can try, but it's not 100% consistent with the rules. One example is that the online game lets you make moves that leave you without a ring, which isn't allowed (if a player wants to end the game, they can just resign).  Another example is that the online game lets you choose a piece whose center is off the board (in columns a or t, or in rows 1 or 20), which isn't allowed.
