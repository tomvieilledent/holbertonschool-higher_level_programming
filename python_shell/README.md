# Simple Shell - Python Version

A Python reimplementation of the Holberton School Simple Shell project, originally written in C.

## Description

This is a minimalist implementation of a UNIX shell that reads commands from standard input and executes them. It replicates basic functionality of shells like `sh`, including command execution, built-in commands, and PATH resolution.

## Features

- Display a prompt and wait for user input
- Execute commands from PATH or by absolute/relative path
- Built-in commands: `exit` and `env`
- Signal handling (Ctrl+C displays a new prompt instead of exiting)
- Works in both interactive and non-interactive mode
- Error handling with appropriate messages

## Usage

### Interactive Mode

Run the shell:
```bash
./hsh.py
```

Or using Python directly:
```bash
python3 hsh.py
```

Then enter commands at the prompt:
```bash
$ ls
file1 file2 file3
$ pwd
/home/user/holbertonschool-higher_level_programming
$ /bin/echo "Hello World"
Hello World
$ exit
```

### Non-Interactive Mode

You can also pipe commands into the shell:
```bash
$ echo "ls -l" | ./hsh.py
```

Or redirect from a file:
```bash
$ ./hsh.py < commands.txt
```

## Built-in Commands

### exit
Exits the shell with the given exit status (default is 0).

```bash
$ exit
$ exit 1
```

### env
Prints all environment variables.

```bash
$ env
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOME=/root
USER=root
...
```

## Error Handling

The shell provides appropriate error messages:

```bash
$ nonexistentcommand
./hsh: 1: nonexistentcommand: not found

$ /path/to/nonexistent
./hsh: 1: /path/to/nonexistent: not found
```

## Implementation Details

### Modules and Functions

- `display_prompt()`: Displays the shell prompt if input is from a terminal
- `read_line()`: Reads a line from standard input
- `clean_line(line)`: Removes leading/trailing whitespace from input
- `get_path(envp)`: Retrieves and splits the PATH environment variable
- `handle_env(envp)`: Prints all environment variables
- `split_command(line)`: Splits a command line into tokens
- `exec_cmd(cmd, argv, envp)`: Executes a command using subprocess
- `exec_from_path(argv, envp)`: Searches and executes a command from PATH
- `execute_command(line, envp)`: Parses and executes a command
- `handle_sigint(signum, frame)`: Handles the SIGINT signal (Ctrl+C)
- `main()`: Main entry point for the shell

## Signal Handling

The shell handles SIGINT (Ctrl+C) gracefully by displaying a new prompt instead of exiting:

```bash
$ ^C
$ 
```

## Comparison with C Version

This Python implementation maintains the same structure and functionality as the original C version, with the following adaptations:

| Feature | C Version | Python Version |
|---------|-----------|-----------------|
| Process forking | `fork()` | `subprocess.run()` |
| Command execution | `execve()` | `subprocess.run()` |
| Memory management | Manual (malloc/free) | Automatic (Python GC) |
| Signal handling | `signal()` | `signal.signal()` |
| Environment access | Function parameter | `os.environ` |
| String tokenization | `strtok()` | `str.split()` |
| File I/O | `write()` syscall | `sys.stdout.write()` |

## Requirements

- Python 3.x

## Differences from C Version

1. **Memory Management**: Python handles memory automatically
2. **String Handling**: Python's built-in string methods vs C's manual string manipulation
3. **Process Management**: Using subprocess module instead of fork/execve
4. **Environment Variables**: Using os.environ dictionary instead of envp array
5. **File Checking**: Using os.path functions instead of access() syscall

## Author

Python version based on the original C implementation from Holberton School.
