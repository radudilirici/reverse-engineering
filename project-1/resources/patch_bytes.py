import idaapi

with open('./function.out', 'rb') as f:
    addr = 0x401842
    byte = f.read(1)
    while byte:
        idaapi.patch_byte(addr, ord(byte))
        byte = f.read(1)
        addr += 1
