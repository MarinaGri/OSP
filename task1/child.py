from os     import getpid, getppid, _exit
from sys    import argv
from time   import sleep
from random import randint

s = int(argv[1])
print(f'Child[{getpid()}]: I am started. My PID {getpid()}. Parent PID {getppid()}.')
sleep(s)
print(f'Child[{getpid()}]: I am ended. PID {getpid()}. Parent PID {getppid()}.')
_exit(randint(0, 1))
