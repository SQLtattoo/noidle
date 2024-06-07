# NoIdle

NoIdle is a simple Python utility that simulates user input to prevent your computer from becoming idle, so that lab environment does not become inactive. It moves the mouse cursor and types messages at regular intervals to keep the system active. The pool of messages is in the code and has some fun messages to bring the energy and the spirit high of technical trainers.

## Features
- Simulates mouse movements to prevent idleness.
- Types motivational messages in the console.
- Optional beep sound with each event.
- Customizable interval between simulated inputs.
- Gracefully handles exit signals (Ctrl+C).

## Requirements
Python and Windows OS

## Installation

Clone the repository:
```bash
git clone https://github.com/sqltattoo/NoIdle.git
```

Navigate to the directory:
```bash
cd NoIdle
```

## Usage

Run the script with default settings:
```bash
python NoIdle.py
```

Customize the interval (in seconds):
```bash
python NoIdle.py --interval 60
```

Enable beep sound:
```bash
python NoIdle.py --beep
```

Combine custom interval and beep sound:
```bash
python NoIdle.py --interval 60 --beep
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
