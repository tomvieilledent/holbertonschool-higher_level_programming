import os, sys, subprocess
from builtin_cmds import is_builtin, execute_builtin

def execute_command(line, envp=os.environ):
    argv = line.split()
    if not argv:
        return 0
    cmd = argv[0]
    
    if is_builtin(cmd):
        return execute_builtin(cmd, argv, envp)
    
    if "/" in cmd:
        if os.access(cmd, os.X_OK):
            return subprocess.run([cmd] + argv[1:], env=envp).returncode
        print(f"./hsh: 1: {cmd}: not found", file=sys.stderr)
        return 127
    
    for d in envp.get("PATH", "").split(":"):
        full = os.path.join(d, cmd)
        if os.access(full, os.X_OK):
            return subprocess.run([full] + argv[1:], env=envp).returncode
    
    print(f"./hsh: 1: {cmd}: not found", file=sys.stderr)
    return 127
