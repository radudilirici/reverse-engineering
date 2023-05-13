from pwn import *


io = process(["gdb", "./task1"])
io.sendline("b *main+211")
io.sendline("b *main+343")
io.sendline("r")

io.recvuntil(b"Enter password:")

message = cyclic(60)
io.sendline(message)

io.interactive()
