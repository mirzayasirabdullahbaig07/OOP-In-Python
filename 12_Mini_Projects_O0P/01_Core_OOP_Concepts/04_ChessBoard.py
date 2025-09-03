"""
Project: Movie Booking System with OOP in Python

Category: Core OOP Concepts

Explanation:
------------
This project simulates a simple Movie Booking System using Object-Oriented Programming concepts.  
We demonstrate:
    - Classes and Objects
    - Inheritance
    - Polymorphism
    - Encapsulation

Main Classes:
1. Seat
   - Attributes: number, seat_type, is_booked
   - Methods: book() → marks the seat as booked

2. Movie
   - Attributes: title, price
   - Represents the movie being booked

3. Payment (Base Class)
   - Method: pay(amount)
   - Abstract class for different payment types

4. Derived Payment Classes: CardPayment, WalletPayment
   - Override the pay() method
   - Demonstrates Polymorphism (different behavior for the same interface)

5. BookingSystem
   - Maintains list of seats
   - Provides methods: select_seats(), confirm_booking()
   - Handles the overall booking flow (seat selection + payment + confirmation)

OOP Concepts Used:
------------------
1. Encapsulation:
   - Each class manages its own data (e.g., Seat knows its own booking status).  

2. Abstraction:
   - Payment details are hidden behind the common pay() method.  

3. Inheritance:
   - Payment subclasses (CardPayment, WalletPayment) inherit from Payment.  

4. Polymorphism:
   - Different payment methods (Card, Wallet) use the same interface pay(), but behave differently.  

Note:
-----
This is a simplified simulation for learning OOP, not a production-level booking system.  
It demonstrates how seat selection, booking, and payment logic can be modeled using classes.
"""

# ---------- Seat ----------
class Seat:
    def __init__(self, number, seat_type="Standard"):
        self.number = number
        self.seat_type = seat_type
        self.is_booked = False

    def book(self):
        if self.is_booked:
            return False
        self.is_booked = True
        return True


# ---------- Movie ----------
class Movie:
    def __init__(self, title, price):
        self.title = title
        self.price = price


# ---------- Payment (Polymorphism) ----------
class Payment:
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Card.")
        return True


class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Wallet balance.")
        return True


# ---------- Booking System ----------
class BookingSystem:
    def __init__(self, movie, total_seats):
        self.movie = movie
        self.seats = [Seat(i + 1) for i in range(total_seats)]

    def select_seats(self, seat_numbers):
        selected = []
        for num in seat_numbers:
            seat = self.seats[num - 1]
            if seat.book():
                selected.append(seat)
            else:
                print(f"Seat {seat.number} is already booked!")
        return selected

    def confirm_booking(self, seats, payment_method: Payment):
        if not seats:
            print("No seats selected.")
            return
        total = self.movie.price * len(seats)
        if payment_method.pay(total):
            print(f"Booking confirmed for {self.movie.title}. Seats: {[s.number for s in seats]}")
        else:
            print("Payment failed. Booking cancelled.")


# ---------- Example Usage ----------
if __name__ == "__main__":
    movie = Movie("Inception", price=300)
    system = BookingSystem(movie, total_seats=5)

    # Select seats
    selected = system.select_seats([1, 2])

    # Pay with wallet
    system.confirm_booking(selected, WalletPayment())

    # Try booking same seat again
    selected2 = system.select_seats([2, 3])
    system.confirm_booking(selected2, CardPayment())


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
