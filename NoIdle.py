import ctypes
import time
import random
import winsound
import argparse
import os
import signal
import sys

# Load the user32.dll library
user32 = ctypes.windll.user32

# Define the input structure
class KEYBDINPUT(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", ctypes.POINTER(ctypes.c_ulong))]

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = [("ki", KEYBDINPUT)]
    _anonymous_ = ("_input",)
    _fields_ = [("type", ctypes.c_ulong), ("_input", _INPUT)]

# Pool of nice messages about Microsoft Technical Trainers
messages = [
    "MTTs rule in learning!",
    "Your dedication to teaching is inspiring!",
    "You are a true expert in tech education!",
    "You make complex topics easy to understand!",
    "Your training sessions are always engaging!",
    "Thank you for your invaluable guidance!",
    "Your expertise makes a huge difference!",
    "Learning from you is always a pleasure!",
    "Awesome trainers like you are rare gems!",
    "You are the best of the best in tech training!",
    "Your training sessions are always top-notch!",
    "You are a true master of tech education!",
    "Your passion for teaching is truly remarkable!",
    "You are the cornerstone of tech education!",
    "Your passion for teaching is contagious!",
    "Your training skills are second to none!",
    "You are transforming tech training for the better!",
    "Keep up the amazing work!"
]

def simulate_mouse_move():
    # Move the mouse to a random nearby position with larger movements
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    user32.mouse_event(0x0001, x, y, 0, 0)

def print_message():
    # Print a random message from the pool to the console
    text = random.choice(messages)
    print(text+"\n")

def make_beep():
    # Make a beep sound
    winsound.Beep(1000, 200)  # Frequency 1000 Hz, Duration 200 ms

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def signal_handler(sig, frame):
    print("\n\nExiting gracefully. Until next time...")
    sys.exit(0)

def prevent_idle(beep=False, interval_seconds=30):
    while True:
        # Clear the console and print a message
        clear_console()
        print_message()
        
        # Countdown timer
        for i in range(interval_seconds, 0, -1):
            print(f"\rNext event in T-{i} seconds", end="")
            time.sleep(1)
        
        # Simulate mouse movement
        simulate_mouse_move()
        if beep:
            make_beep()

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Prevent the computer from becoming idle by simulating user input.")
    parser.add_argument('--beep', dest='beep', action='store_true', help="Enable beep sound")
    parser.add_argument('--interval', type=int, default=30, help="Set the interval in seconds between actions (default: 30 seconds)")
    args = parser.parse_args()

    # Handle graceful exit
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Run the prevent_idle function with the provided or default parameters
    prevent_idle(beep=args.beep, interval_seconds=args.interval)
