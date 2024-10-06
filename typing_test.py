import time
import sys
import termios
import tty

def calculate_wpm(text, elapsed_time):
    words = len(text) / 5  # Assuming average word length of 5 characters
    minutes = elapsed_time / 60
    return round(words / minutes, 2)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def typing_test():
    print("Start typing. Press Enter to end the test. Use Backspace to correct mistakes.")
    start_time = time.time()
    typed_text = []

    while True:
        char = getch()
        if char == '\r' or char == '\n':  # Enter key
            break
        elif char == '\x7f':  # Backspace
            if typed_text:
                typed_text.pop()
                sys.stdout.write('\b \b')  # Move cursor back, write space, move cursor back again
                sys.stdout.flush()
        else:
            sys.stdout.write(char)
            sys.stdout.flush()
            typed_text.append(char)

    end_time = time.time()
    elapsed_time = end_time - start_time
    full_text = ''.join(typed_text)
    wpm = calculate_wpm(full_text, elapsed_time)
    print(f"\n\nTest ended. Your typing speed: {wpm} WPM")

if __name__ == "__main__":
    typing_test()
