# Tic Tac Toe game
# This is two player game and each player can enter their move one by one
# This program will choose one of the play to go first randomly

import random

# This class has all the functions to manage Tic Tac Toe board functionality 
class BoardClass():
    def __init__(self):
        self.board = [' '] * 10

    # this function will draw the board
    def drawBoard(self):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + self.board[7] + ' | ' + self.board[8] + ' | ' + self.board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[4] + ' | ' + self.board[5] + ' | ' + self.board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.board[1] + ' | ' + self.board[2] + ' | ' + self.board[3])
        print('   |   |')

    # checks in space is free on the board
    def isSpaceFree(self, move):
        # Return true if the passed move is free on the passed board.
        return self.board[move] == ' '

    # make the move on the board
    def makeMove(self, letter, move):
        self.board[move] = letter

    # checks if board is full
    def isBoardFull(self):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    # checks if given player is winner
    def isWinner(self, le):   
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((self.board[7] == le and self.board[8] == le and self.board[9] == le) or # across the top
        (self.board[4] == le and self.board[5] == le and self.board[6] == le) or # across the middle
        (self.board[1] == le and self.board[2] == le and self.board[3] == le) or # across the bottom
        (self.board[7] == le and self.board[4] == le and self.board[1] == le) or # down the left side
        (self.board[8] == le and self.board[5] == le and self.board[2] == le) or # down the middle
        (self.board[9] == le and self.board[6] == le and self.board[3] == le) or # down the right side
        (self.board[7] == le and self.board[5] == le and self.board[3] == le) or # diagonal
        (self.board[9] == le and self.board[5] == le and self.board[1] == le)) # diagonal

# this class help 2 players play against each other
class Game():
    def __init__(self):
        print('Welcome to Tic Tac Toe!')

    # this is the main function lets both playes play with each other
    def play(self):
        while True:
            # Reset the board
            theBoard = BoardClass()
            player1Letter, player2Letter = self.inputPlayerLetter()
            turn = self.whoGoesFirst()
            print('The ' + turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player1':
                    # Player's turn.
                    move = self.getPlayerMove(theBoard)
                    theBoard.makeMove(player1Letter, move)
                    theBoard.drawBoard()

                    if theBoard.isWinner(player1Letter):
                        print('Hooray! You have won the game!')
                        gameIsPlaying = False
                    else:
                        if theBoard.isBoardFull():
                            theBoard.drawBoard()
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player2'
                else:
                    # player2's turn.
                    move = self.getPlayerMove(theBoard)
                    theBoard.makeMove(player2Letter, move)
                    theBoard.drawBoard()

                    if theBoard.isWinner(player2Letter):
                        print('The player2 has beaten you! You lose.')
                        gameIsPlaying = False
                    else:
                        if theBoard.isBoardFull():
                            theBoard.drawBoard()
                            print('The game is a tie!')
                            break
                        else:
                            turn = 'player1'
            if not self.playAgain():
                break
    # this function takes player letter            
    def inputPlayerLetter(self):
        # Lets the player type which letter they want to be.
        # Returns a list with the player1's letter as the first item, and the player2's letter as the second.
        letter = ''
        while not (letter == 'X' or letter == 'O'):
            print('Do you want to be X or O?')
            letter = input().upper()

        # the first element in the tuple is the player1's letter, the second is the player2's letter.
        if letter == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']

    # this function randomely choose one of the player to go first
    def whoGoesFirst(self):
        # Randomly choose the player who goes first.
        if random.randint(0, 1) == 0:
            return 'player2'
        else:
            return 'player1'

    # players can choose to play again
    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    # this function lets player input the next move
    def getPlayerMove(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not board.isSpaceFree(int(move)):
            print('What is your next move? (1-9)')
            move = input()
        return int(move)

game = Game()
game.play()