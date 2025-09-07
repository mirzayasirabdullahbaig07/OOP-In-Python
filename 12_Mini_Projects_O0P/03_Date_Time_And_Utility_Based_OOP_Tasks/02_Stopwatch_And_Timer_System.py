"""
Project: Stopwatch and Timer (OOP in Python)

Category: Date, Time & Utility-Based OOP Tasks

Explanation:
------------
This project demonstrates how to create a Stopwatch (for counting elapsed time)
and a Timer (for countdowns) using OOP principles.

OOP Concepts Used:
------------------
1. Encapsulation → Start/stop/reset logic is hidden inside classes.  
2. Abstraction   → Base class defines interface (start, stop, reset).  
3. Inheritance   → Stopwatch and Timer both extend the base Clock class.  
4. Polymorphism  → run() behaves differently for Stopwatch (count up) vs Timer (count down).  

Main Classes:
-------------
1. Clock (Abstract Base Class)
   - Defines the interface for time-based operations.

2. Stopwatch (Derived Class)
   - Tracks elapsed time.
   - Provides start, stop, reset, and elapsed time.

3. Timer (Derived Class)
   - Counts down from a given duration.
   - Provides start, stop, reset, and remaining time.
"""

import time
from abc import ABC, abstractmethod

# ---------- Abstraction ----------
class Clock(ABC):
    def __init__(self):
        self._running = False

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def reset(self):
        pass

# ---------- Stopwatch ----------
class Stopwatch(Clock):
    def __init__(self):
        super().__init__()
        self._start_time = None
        self._elapsed = 0

    def start(self):
        if not self._running:
            self._running = True
            self._start_time = time.time()
            print("⏱ Stopwatch started.")

    def stop(self):
        if self._running:
            self._elapsed += time.time() - self._start_time
            self._running = False
            print("⏱ Stopwatch stopped.")

    def reset(self):
        self._running = False
        self._start_time = None
        self._elapsed = 0
        print("⏱ Stopwatch reset.")

    def elapsed_time(self):
        if self._running:
            return self._elapsed + (time.time() - self._start_time)
        return self._elapsed

# ---------- Timer ----------
class Timer(Clock):
    def __init__(self, duration):
        super().__init__()
        self._duration = duration  # seconds
        self._remaining = duration
        self._start_time = None

    def start(self):
        if not self._running and self._remaining > 0:
            self._running = True
            self._start_time = time.time()
            print(f"⏲ Timer started for {self._remaining:.2f} seconds.")

    def stop(self):
        if self._running:
            elapsed = time.time() - self._start_time
            self._remaining -= elapsed
            self._running = False
            print(f"⏲ Timer stopped. Remaining: {self._remaining:.2f} seconds.")

    def reset(self):
        self._running = False
        self._remaining = self._duration
        self._start_time = None
        print("⏲ Timer reset.")

    def remaining_time(self):
        if self._running:
            elapsed = time.time() - self._start_time
            return max(0, self._remaining - elapsed)
        return self._remaining

# ==============================
# Example Usage
# ==============================
if __name__ == "__main__":
    # Stopwatch demo
    sw = Stopwatch()
    sw.start()
    time.sleep(2)
    sw.stop()
    print(f"Elapsed Time: {sw.elapsed_time():.2f} seconds")
    sw.reset()

    print("\n------------------\n")

    # Timer demo
    t = Timer(5)  # 5-second timer
    t.start()
    time.sleep(2)
    print(f"Remaining: {t.remaining_time():.2f} seconds")
    t.stop()
    t.reset()
