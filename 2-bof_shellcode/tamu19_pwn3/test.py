from pwn import *

# Start a process
bash = process('bash')

# Attach the debugger
gdb.attach(bash, '''
set follow-fork-mode child
break execve
continue
''')

# Interact with the process
bash.sendline('whoami')

