import sys, signal

def display_prompt():
    if sys.stdin.isatty():
        sys.stdout.write("$ ")
        sys.stdout.flush()

def read_line():
    try:
        return input()
    except EOFError:
        if sys.stdin.isatty():
            sys.stdout.write("\n")
        return None

def handle_sigint(s, f):
    sys.stdout.write("\n$ ")
    sys.stdout.flush()

def setup_signal():
    signal.signal(signal.SIGINT, handle_sigint)
