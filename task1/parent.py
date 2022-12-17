from os     import getpid, getppid, wait, execv, fork
from sys    import argv
from random import randint

n = int(argv[1])
children = []
for i in range(n):
    child_pid = fork()
    if child_pid != 0:
        print(f'Parent[{getpid()}]: I ran children process with PID {child_pid}.')
        children.append(child_pid)
    else:
        execv('/usr/bin/python3', ['python3', 'child.py', str(randint(5, 10))])

while children:
    child_pid, exit_code = wait()
    if child_pid != 0:
        print(f'Parent[{getpid()}]: Child with PID {child_pid} terminated. Exit Status {exit_code}.')
        children.remove(child_pid)
        if exit_code != 0:
            child_pid = fork()
            if child_pid != 0:
                print(f'Parent[{getpid()}]: I ran children process with PID {child_pid}.')
                children.append(child_pid)
            else:
                execv('/usr/bin/python3', ['python3', 'child.py', str(randint(5, 10))])
