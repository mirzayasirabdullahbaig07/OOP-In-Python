"""
Project: ChessBoard Simulation with OOP in Python

Category: Core OOP Concepts

Explanation:
------------
This project simulates a ChessBoard and pieces using Object-Oriented Programming concepts.
We demonstrate:
    - Classes and Objects
    - Inheritance
    - Polymorphism
    - Encapsulation

Main Classes:
1. ChessPiece (Base class)
   - Common attributes: name, color, position
   - Common methods: move()

2. Derived Classes: Pawn, Rook, Knight, Bishop, Queen, King
   - Each overrides the move() method with simple rules (not full chess rules, but enough to simulate).

3. ChessBoard
   - Maintains an 8x8 board
   - Places pieces on the board
   - Provides methods to move pieces
   - Prints the current state of the board

Note:
This is a simplified simulation to demonstrate OOP concepts, not a complete chess engine.

"""

# Base Class
class ChessPiece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position  # (row, col)

    def move(self, new_position):
        """Default move (can be overridden by subclasses)."""
        self.position = new_position

    def __str__(self):
        return f"{self.color[0]}{self.name[0]}"


# Derived Classes
class Pawn(ChessPiece):
    def move(self, new_position):
        row, col = self.position
        new_row, new_col = new_position
        # Simplified: Pawn can move one step forward
        if col == new_col and ((self.color == "White" and new_row == row - 1) or (self.color == "Black" and new_row == row + 1)):
            self.position = new_position
        else:
            print("Invalid Pawn move!")


class Rook(ChessPiece):
    def move(self, new_position):
        row, col = self.position
        new_row, new_col = new_position
        # Rook moves straight lines
        if row == new_row or col == new_col:
            self.position = new_position
        else:
            print("Invalid Rook move!")


class Knight(ChessPiece):
    def move(self, new_position):
        row, col = self.position
        new_row, new_col = new_position
        # L-shape move
        if (abs(new_row - row), abs(new_col - col)) in [(2, 1), (1, 2)]:
            self.position = new_position
        else:
            print("Invalid Knight move!")


class Bishop(ChessPiece):
    def move(self, new_position):
        row, col = self.position
        new_row, new_col = new_position
        # Bishop moves diagonally
        if abs(new_row - row) == abs(new_col - col):
            self.position = new_position
        else:
            print("Invalid Bishop move!")


class Queen(ChessPiece):
    def move(self, new_position):
        row, col = self.position
        new_row, new_col = new_position
        # Queen moves straight or diagonally
        if row == new_row or col == new_col or abs(new_row - row) == abs(new_col - col):
            self.position = new_position
        else:
            print("Invalid Queen move!")


class King(ChessPiece):
    def move(self, new_position):
        row, col = self.position
        new_row, new_col = new_position
        # King moves one square any direction
        if max(abs(new_row - row), abs(new_col - col)) == 1:
            self.position = new_position
        else:
            print("Invalid King move!")


# ChessBoard Class
class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
        # Place a few pieces (simplified setup)
        self.board[6][0] = Pawn("Pawn", "White", (6, 0))
        self.board[0][0] = Rook("Rook", "Black", (0, 0))
        self.board[7][1] = Knight("Knight", "White", (7, 1))
        self.board[0][2] = Bishop("Bishop", "Black", (0, 2))
        self.board[7][3] = Queen("Queen", "White", (7, 3))
        self.board[0][4] = King("King", "Black", (0, 4))

    def move_piece(self, start, end):
        row, col = start
        piece = self.board[row][col]
        if piece:
            piece.move(end)
            new_row, new_col = piece.position
            # Update board
            self.board[new_row][new_col] = piece
            self.board[row][col] = None
        else:
            print("No piece at that position!")

    def display(self):
        for row in self.board:
            print([str(piece) if piece else "--" for piece in row])
        print("\n")


# Example Usage
if __name__ == "__main__":
    board = ChessBoard()
    print("Initial Board:")
    board.display()

    print("Move White Pawn from (6,0) to (5,0):")
    board.move_piece((6, 0), (5, 0))
    board.display()

    print("Move Black Rook from (0,0) to (0,5):")
    board.move_piece((0, 0), (0, 5))
    board.display()

    print("Trying Invalid Knight Move (7,1) to (5,1):")
    board.move_piece((7, 1), (5, 1))
    board.display()
