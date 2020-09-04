# Author: ShengTso Andrew Wu
# Date: 05/25/2020
# Description: A portfolio project for CS162 that implements a chess variant - Gess Game.

class GessGame():
    """
    Represents a GessGame item with board, current game state, and current turn
    """
    def __init__(self):
        """
        Creates new GessGame item with turn initialized to Black, game state to unfinished, and board to
        default positions. Sets game state to default of black. Board is set to default position.
        """
        self._turn = 'B'                    #Game starts with Black by default
        self._gameState = 'UNFINISHED'
        self._board = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', 'W', '', 'W', '', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '', 'W', '', 'W', '', ''],
                       ['', 'W', 'W', 'W', '', 'W', '', 'W', 'W', 'W', 'W', '', 'W', '', 'W', '', 'W', 'W', 'W', ''],
                       ['', '', 'W', '', 'W', '', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '', 'W', '', 'W', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', 'W', '', '', 'W', '', '', 'W', '', '', 'W', '', '', 'W', '', '', 'W', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', 'B', '', '', 'B', '', '', 'B', '', '', 'B', '', '', 'B', '', '', 'B', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
                       ['', '', 'B', '', 'B', '', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '', 'B', '', 'B', '', ''],
                       ['', 'B', 'B', 'B', '', 'B', '', 'B', 'B', 'B', 'B', '', 'B', '', 'B', '', 'B', 'B', 'B', ''],
                       ['', '', 'B', '', 'B', '', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '', 'B', '', 'B', '', ''],
                       ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']]

    def resign_game(self):
        """
        If the resign game method is triggered, if game state is still unfinished, find the current player and
        set game state to opposite player having won. If game state not unfinished, then return False.
        """
        if self.get_game_state() == 'UNFINISHED':
            if self.get_turn() == 'B':
                self.set_game_state('WHITE_WON')
            else:
                self.set_game_state('BLACK_WON')
        else:
            return False

    def get_turn(self):
        """
        Getter for current player private attribute "Turn". Returns turn.
        """
        return self._turn

    def get_opponent(self):
        """
        Returns the opponent of current player. Calls get_turn and returns opposite player.
        """
        if self.get_turn() == 'B':
            return 'W'
        else:
            return 'B'

    def set_next_turn(self):
        """
        Setter method to set the next turn. Calls get turn and sets opposite player to next turn.
        """
        if self.get_turn() == 'B':
            self._turn = 'W'
        else:
            self._turn = 'B'

    def get_game_state(self):
        """
        Getter for current game state. Returns gameState
        """
        return self._gameState

    def set_game_state(self, state):
        """
        Setter method for game state. Receives state and sets game state.
        """
        self._gameState = state

    def get_xAxis(self, x_Value):
        """
        Method to convert the letters that represents x axis to numbers. Returns corresponding xValue. If key not
        in dictionary, input is invalid and return false.
        """
        dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
                      "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20}
        if x_Value in dictionary:
            return dictionary[x_Value]
        else:
            return False

    def get_yAxis(self, y_Value):
        """
        Method to convert the y axis to rows with 0 on top and 19 on bottom. Returns corresponding yValue. If key not
        in dictionary, input is invalid and return false.
        """
        dictionary = {20: 0, 19: 1, 18: 2, 17: 3, 16: 4, 15: 5, 14: 6, 13: 7, 12: 8, 11: 9, 10: 10,
                      9: 11, 8: 12, 7: 13, 6: 14, 5: 15, 4: 16, 3: 17, 2: 18, 1: 19}
        if y_Value in dictionary:
            return dictionary[y_Value]
        else:
            return False

    def print_board(self):
        """
        Method to print current board to assist with testing code.
        """
        matrix = self.get_board()
        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

    def get_board(self):
        """
        Getter method for returning board
        """
        return self._board

    def search_Ring(self, player):
        """
        Method to search for an existing ring. Iterate through the board using For Loop until a piece is found
        that matches the player ('W' or 'B'). When a player piece found, search for a ring starting from that
        piece position. Ring needs to not have a center piece but all the perimeter pieces of 3x3. If an existing
        ring is found, return True. If not, continue iterating. If end of board is reached, return False.
        """
        countRow = -1
        for line in self.get_board():
            countRow += 1
            countColumn = 0
            for piece in line:
                if piece == player:
                    try:
                        if self.get_board()[countRow][countColumn+1] == player:
                            if self.get_board()[countRow][countColumn+2] == player:
                                if self.get_board()[countRow+1][countColumn] == player:
                                    if self.get_board()[countRow +1][countColumn+1] == '':
                                        if self.get_board()[countRow+1][countColumn+2] == player:
                                            if self.get_board()[countRow+2][countColumn] == player:
                                                if self.get_board()[countRow+2][countColumn+1] == player:
                                                    if self.get_board()[countRow+2][countColumn+2] == player:
                                                        return True
                    except:
                        continue
                countColumn += 1
        return False

    def make_move_conversion(self, pos1, pos2):
        """
        Takes position 1 and position 2 from make move. Converts the start/end columns and rows. Sends to
        check valid move to validate move. If not valid move, return False. Else, make move and return true.
        """
        startColumn = self.get_xAxis(pos1[:1]) - 1
        startRow = self.get_yAxis(int(pos1[1:]))
        endColumn = self.get_xAxis(pos2[:1]) - 1
        endRow = self.get_yAxis(int(pos2[1:]))

        if self.check_valid_move(startColumn, startRow, endColumn, endRow) != True:
            return False
        else:
            self.move_footPrint(startColumn, startRow, endColumn, endRow)
            return True

    def make_move(self, position1, position2):
        """
        Method will:
        1) check game state (by calling game state) is 'UNFINISHED'. If not, return False.
        2) check the move is valid by sending position1 and position 2 to make move conversion. That method will convert
        the positions to corresponding row/column in integer form. Then send to check_valid method. If not valid, return False.
        If Valid, make move conversion will send row/column to move footprint to make move.
        3) check opponent still has a valid ring to continue ring by calling search_Ring(opposite player). If
        this returns False, set game state to current turn winner via set_game_state(current player win)
        4) if game state still 'UNFINISHED', call set_next_turn to start next turn.
        """
        if self.get_game_state() != 'UNFINISHED':
            #print("Game status failure: Not Unfinished")
            return False
        """
        2) check the move is valid by sending position1 and position 2 to make move conversion. That method will convert
        the positions to corresponding row/column in integer form. Then send to check_valid method. If not valid, return False. 
        If Valid, make move conversion will send row/column to move footprint to make move. 
        """
        if self.make_move_conversion(position1, position2) != True:
            return False
        """
        3) check opponent still has a valid ring to continue ring by calling search_Ring(opposite player). If
        this returns False, set game state to current turn winner via set_game_state(current player win)
        """
        if self.search_Ring(self.get_opponent()) != True:
            if self.get_turn() == 'B':
                self.set_game_state('BLACK_WON')
            else:
                self.set_game_state('WHITE_WON')
        """
        4) if game state still 'UNFINISHED', call set_next_turn to start next turn.
        """
        if self.get_game_state() == 'UNFINISHED':
            self.set_next_turn()

        return True

    def check_valid_move(self, startColumn, startRow, endColumn, endRow):
        """
        1) Check end position does not go beyond 2-19 and B-S on board. If not, return False
        2) Check starting 3x3 footprint is all equal to current player. If not, return False
        3) CCheck the intended direction of move is valid. For example: If footprint wants to move up on board,
            make sure there is a piece in upper most middle of footprint. If not valid, return False
        4) Check distance of move. If footprint does not have middle piece, limit to 3 space move. If contains
        a center piece, unlimited movement distance.
        5) Check for obstacles in the way. Iterate in the direction of the move and check the footprint does not
            touch any other pieces. Stop the check one iteration before last move since last move could "capture"
            pieces. Both current player and opponent player pieces can be captured.
        6) Copy the board to temp board and check the move does not leave the player without a valid ring by
            calling search_Ring(self.get_turn()). Restore the board and return False if move leaves player w.o
            ring.
        7) If all valid, return True
        """
        try:
            """
            1) Check end position does not go beyond 2-19 and B-S on board. If not, return False
            """
            if endColumn < 1 or endColumn > 18:
                #print("failed board limit: end")
                return False
            elif endRow < 1 or endRow > 18:
                #print("failed board limit: end")
                return False
            elif startColumn < 1 or startColumn > 18:
                #print("failed board limit: start")
                return False
            elif startRow < 1 or startRow > 18:
                #print("failed board limit: start")
                return False
            """
            2) Check starting 3x3 footprint is all equal to current player. If not, return False
            """
            for indexRow in range(-1, 2):
                for indexColumn in range(-1, 2):
                    if self.get_board()[startRow + indexRow][startColumn + indexColumn] == self.get_opponent():
                        #print("Failed 3x3 footprint test: contains opponent pieces")
                        return False
            """
            3) Check the intended direction of move is valid. For example: If footprint wants to move up on board, 
            make sure there is a piece in upper most middle of footprint. If not valid, return False
            """
            direction = self.direction(startColumn, startRow, endColumn, endRow)
            if direction == 'N':
                if self.get_board()[startRow - 1][startColumn] != self.get_turn():
                    #print("No Piece to go N")
                    return False
            elif direction == 'S':
                if self.get_board()[startRow + 1][startColumn] != self.get_turn():
                    #print("No Piece to go S")
                    return False
            elif direction == 'W':
                if self.get_board()[startRow][startColumn - 1] != self.get_turn():
                    #print("No Piece to go W")
                    return False
            elif direction == 'E':
                if self.get_board()[startRow][startColumn + 1] != self.get_turn():
                    #print("No Piece to go E")
                    return False
            elif direction == 'NE':
                if self.get_board()[startRow - 1][startColumn + 1] != self.get_turn():
                    #print("No Piece to go NE")
                    return False
            elif direction == 'SE':
                if self.get_board()[startRow + 1][startColumn + 1] != self.get_turn():
                    #print("No Piece to go SE")
                    return False
            elif direction == 'NW':
                if self.get_board()[startRow - 1][startColumn - 1] != self.get_turn():
                    #print("No Piece to go NW")
                    return False
            elif direction == 'SW':
                if self.get_board()[startRow + 1][startColumn - 1] != self.get_turn():
                    #print("No Piece to go SW")
                    return False
            """
            4) Check distance of move. If footprint does not have middle piece, limit to 3 space move. If contains
            a center piece, unlimited movement distance.
            """
            if self.get_board()[startRow][startColumn] != self.get_turn():
                if abs(endColumn - startColumn) > 3 or abs(endRow - startRow) > 3:
                    #print("Distance failure")
                    return False
            """
            5) Check for obstacles in the way. Iterate in the direction of the move and check the footprint does not
            touch any other pieces. Stop the check one iteration before last move since last move could "capture" 
            pieces. Both current player and opponent player pieces can be captured. 
            """
            if direction == 'N':
                for indexRow in range(2, abs(endRow - startRow)):
                    if self.get_board()[startRow - indexRow][startColumn] != '':
                        #print("Move is N obstructed")
                        return False
            elif direction == 'S':
                for indexRow in range(2, abs(endRow - startRow)):
                    if self.get_board()[startRow + indexRow][startColumn] != '':
                        #print("Move is S obstructed")
                        return False
            elif direction == 'E':
                for indexColumn in range(2, abs(endColumn - startColumn)):
                    if self.get_board()[startRow][startColumn + indexColumn] != '':
                        #print("Move is E obstructed")
                        return False
            elif direction == 'W':
                for indexColumn in range(2, abs(endColumn - startColumn)):
                    if self.get_board()[startRow][startColumn - indexColumn] != '':
                        #print("Move is W obstructed")
                        return False
            elif direction == 'NE':
                for indexRow in range(2, abs(endRow - startRow)):
                    for indexColumn in range(2, abs(endColumn - startColumn)):
                        if self.get_board()[startRow - indexRow][startColumn + indexColumn] != '':
                            #print("Move NE is obstructed")
                            return False
            elif direction == 'SE':
                for indexRow in range(2, abs(endRow - startRow)):
                    for indexColumn in range(2, abs(endColumn - startColumn)):
                        if self.get_board()[startRow + indexRow][startColumn + indexColumn] != '':
                            #print("Move SE is obstructed")
                            return False
            elif direction == 'NW':
                for indexRow in range(2, abs(endRow - startRow)):
                    for indexColumn in range(2, abs(endColumn - startColumn)):
                        if self.get_board()[startRow - indexRow][startColumn - indexColumn] != '':
                            #print("Move NW is obstructed")
                            return False
            elif direction == 'SW':
                for indexRow in range(2, abs(endRow - startRow)):
                    for indexColumn in range(2, abs(endColumn - startColumn)):
                        if self.get_board()[startRow + indexRow][startColumn - indexColumn] != '':
                            #print("Move SW is obstructed")
                            return False
            """
            6) Copy the board to temp board and check the move does not leave the player without a valid ring by 
            calling search_Ring(self.get_turn()). Restore the board and return False if move leaves player w.o 
            ring.            
            """
            tempBoard = [self._board[:] for index in orig]                      #Duplicate nested list
            self.move_footPrint(startColumn, startRow, endColumn, endRow)
            if self.search_Ring(self.get_turn()) != True:
                #print("Leaves player w/o ring")
                self._board = tempBoard
                return False
            self._board = tempBoard

        except:
            pass
        """
        7) If all valid, return True
        """
        return True


    def direction(self, startColumn, startRow, endColumn, endRow):
        """
        Receives starting X, Y and ending X,Y from check valid move. Calculates the direction of movement
        based on coordinates and returns correct direction. For example, if the start and end columns are same,
        and starting row is a higher int than end row, return N.
        """
        if startColumn == endColumn:
            if startRow > endRow:
                return 'N'
            else:
                return 'S'
        elif startRow == endRow:
            if startColumn > endColumn:
                return 'W'
            else:
                return 'E'
        elif startColumn < endColumn:
            if startRow > endRow:
                return "NE"
            else:
                return "SE"
        elif startColumn > endColumn:
            if startRow < endRow:
                return "SW"
            else:
                return "NW"
        else:
            return False

    def move_footPrint(self, startColumn, startRow, endColumn, endRow):
        """
        Receives start x, y and end x,y from check valid. Save the footprint to move to tempFootprint. Reverse the
        list so it can be popped into new location. Clear out old footprint. Pop the tempFootprint to new destination.
        Check the new footprint does not place any pieces outside of bound. If out of bound, clear out the piece.
        """
        try:
            tempFootprint= []
            for indexRow in range(-1, 2, ):
                for indexColumn in range(-1, 2):
                    tempFootprint.append(self.get_board()[startRow + indexRow][startColumn + indexColumn])

            tempFootprint.reverse()

            for indexRow in range(-1, 2, ):
                for indexColumn in range(-1, 2):
                    (self.get_board()[startRow + indexRow][startColumn + indexColumn]) = ''

            for indexRow in range(-1, 2, ):
                for indexColumn in range(-1, 2):
                    self._board[endRow + indexRow][endColumn + indexColumn] = tempFootprint.pop()
                    if endRow + indexRow == 0 or endRow + indexRow == 19 or endColumn + indexColumn == 0 \
                        or endColumn + indexColumn == 19:
                        self._board[endRow + indexRow][endColumn + indexColumn] = ''
        except:
            pass

"""
ADDITIONAL NOTES FOR HALFWAY PROGRESS REPORT

A player makes a legal move that doesn't capture any stones.
    The check valid move method would return True when checking if the move is valid. The move_footprint
    method would move to destination. Last piece of make move method would set to next player's turn and
    the game would continue. 
A player makes a legal move that captures at least one stone (including updating the game state if needed).
    Move footprint would capture or overwrite opponent player stones. Make move would then call search Ring
    to make sure opponent still has a valid ring. If no valid ring is found, set current player as winner. 
    Else continue. 
A player tries to move a "piece" whose 3x3 footprint contains stones belonging to the other player.
    The first part of the make move method would check that the 3x3 footprint contains only pieces that match
    the current player.
A player tries to move a legal "piece", but in a way that it shouldn't be able to move.
    Check valid move would check the various scenarios of the move. For example, if footprint tries to move 
    in a way that would result in center moving off the board, it would flag as invalid move. 
A player resigns.
    Resigns would set the game status to opponent winning.
"""



"""
tester = GessGame()
tester.print_board()
print(tester.make_move('c3', 'b3'))

print(tester.make_move('i18', 'i19'))
tester.print_board()

print(tester.make_move('c3', 'b3'))
print(tester.make_move('o5', 'o13'))
print(tester.make_move('o15', 'o13'))
print(tester.make_move('d10', 'a10'))
print(tester.make_move('b3', 'b17'))
print(tester.make_move('j7', 'h7'))
print(tester.make_move('s14','q14'))
print(tester.make_move('i3', 'i13'))
print(tester.make_move('f15', 'f12'))
print(tester.make_move('i13', 'i16'))
print(tester.make_move('c15','c14'))
print(tester.make_move('i16', 'i17'))
print(tester.make_move('m18', 'm17'))
print(tester.make_move('o18', 'p17'))
print(tester.make_move('i17', 'i18'))
print(tester.make_move('l15', 'l14'))
print(tester.make_move('i18', 'j18'))
tester.print_board()
print(tester.get_game_state())
print(tester.resign_game())
print(tester.get_game_state())"""




