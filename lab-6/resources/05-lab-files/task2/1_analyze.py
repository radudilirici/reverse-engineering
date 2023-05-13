from pwn import *


io = process(["gdb", "./task2"])
io.sendline(b"b *main+355")
io.sendline(b"r")

io.recvuntil(b"Enter password:")

message = flat(
    b'aaaaaaaa\x00',
    cyclic(50)
)
io.sendline(message)

io.interactive()
