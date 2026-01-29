import sys, os

def cmd_exit(argv):
    sys.exit(0)

def cmd_env(argv, envp):
    [print(f"{k}={v}") for k, v in envp.items()]
    return 0

def cmd_cd(argv, envp):
    try:
        os.chdir(argv[1] if len(argv) > 1 else envp.get("HOME", "/"))
        return 0
    except (IndexError, OSError) as e:
        print(f"./hsh: cd: {e}", file=sys.stderr)
        return 1

def cmd_chmod(argv):
    try:
        if len(argv) < 3:
            print("./hsh: chmod: missing operand", file=sys.stderr)
            return 1
        mode = int(argv[1], 8)
        for f in argv[2:]:
            os.chmod(f, mode)
        return 0
    except (ValueError, OSError) as e:
        print(f"./hsh: chmod: {e}", file=sys.stderr)
        return 1

BUILTINS = {
    "exit": cmd_exit,
    "env": cmd_env,
    "cd": cmd_cd,
    "chmod": cmd_chmod
}

def is_builtin(cmd):
    return cmd in BUILTINS

def execute_builtin(cmd, argv, envp=None):
    if cmd == "env":
        return cmd_env(argv, envp or os.environ)
    elif cmd == "cd":
        return cmd_cd(argv, envp or os.environ)
    elif cmd in BUILTINS:
        return BUILTINS[cmd](argv)
    return None
