# OOP Movie Booking System (Simple)

class Seat:
    def __init__(self, number):
        self.number = number
        self.is_booked = False

    def book(self):
        if self.is_booked:
            return False
        self.is_booked = True
        return True


class Movie:
    def __init__(self, title):
        self.title = title


class Payment:
    def __init__(self, method):
        self.method = method

    def pay(self, amount):
        print(f"Payment of {amount} done using {self.method}.")
        return True


class BookingSystem:
    def __init__(self, movie, total_seats, price):
        self.movie = movie
        self.seats = [Seat(i + 1) for i in range(total_seats)]
        self.price = price

    def select_seat(self, seat_number):
        seat = self.seats[seat_number - 1]
        if seat.book():
            print(f"Seat {seat.number} selected.")
            return seat
        else:
            print(f"Seat {seat.number} already booked!")
            return None

    def make_payment(self, seat, method):
        if seat:
            payment = Payment(method)
            if payment.pay(self.price):
                print(f"Booking confirmed for {self.movie.title}, Seat {seat.number}.")
        else:
            print("Payment failed. Seat not booked.")


# Example Usage
movie = Movie("Inception")
system = BookingSystem(movie, total_seats=5, price=300)

seat1 = system.select_seat(2)       # select seat 2
system.make_payment(seat1, "Card")  # pay by card

seat2 = system.select_seat(2)       # try same seat again -> already booked
