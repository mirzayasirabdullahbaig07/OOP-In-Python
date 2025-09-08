"""
Project: Real-Time Log Monitor
Field: DevOps / System Monitoring
Concepts Used: File Handling + OOP (Encapsulation, Abstraction)
"""

import time
import os


class LogMonitor:
    """
    LogMonitor Class:
    -----------------
    - Monitors a log file in real-time (like `tail -f` in Linux).
    - Continuously reads new lines from a given file.
    - Can be extended with filters, alerts, or saving features.
    """

    def __init__(self, filepath: str, interval: float = 1.0):
        """
        Initialize the log monitor.

        :param filepath: Path of the log file to monitor
        :param interval: Time (in seconds) between checks
        """
        self.filepath = filepath
        self.interval = interval
        self._stop_monitoring = False

    def _open_file(self):
        """
        Try opening the file safely.
        Raises FileNotFoundError if file does not exist.
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"Log file '{self.filepath}' does not exist.")
        return open(self.filepath, "r")

    def start(self):
        """
        Start monitoring the log file in real-time.
        Reads new lines as they appear.
        """
        try:
            with self._open_file() as file:
                # Move cursor to end of file (ignore old logs)
                file.seek(0, os.SEEK_END)

                print(f"📜 Monitoring log file: {self.filepath} (Press Ctrl+C to stop)")
                while not self._stop_monitoring:
                    line = file.readline()
                    if line:
                        self.process_line(line.strip())
                    else:
                        time.sleep(self.interval)  # wait before re-checking
        except Exception as e:
            print(f" Error: {e}")

    def process_line(self, line: str):
        """
        Process each new line (customizable).
        Currently, it just prints the log line.
        """
        print(f"➡️ New log entry: {line}")

    def stop(self):
        """
        Stop monitoring the log file.
        """
        self._stop_monitoring = True


# ------------------ Example Usage ------------------ #
if __name__ == "__main__":
    log_file = "app.log"   # Ensure this file exists in the same directory
    monitor = LogMonitor(log_file, interval=0.5)  # Create object

    try:
        monitor.start()   # Start monitoring
    except KeyboardInterrupt:
        # Stop when user presses Ctrl+C
        print("\n Monitoring stopped by user.")
        monitor.stop()
