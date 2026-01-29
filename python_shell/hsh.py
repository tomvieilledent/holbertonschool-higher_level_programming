#!/usr/bin/env python3
"""
Simple Shell - Main entry point
Imports modules and runs the shell loop
"""
import sys, os
from shell import display_prompt, read_line, setup_signal
from executor import execute_command

if __name__ == "__main__":
    setup_signal()
    
    while (line := read_line()) is not None:
        line = line.strip()
        if line:
            folder = os.path.basename(os.getcwd())
            sys.stdout.write(f"$ \033[1;32m{folder}\033[0m ")  # Gras + vert + reset
            print(line)
            execute_command(line)
