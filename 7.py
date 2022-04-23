def main(x):
    A = x & 0b111111111111111
    B = (x >> 15) & 0b11
    C = (x >> 17) & 0b11
    D = (x >> 19) & 0b1111111
    E = (x >> 26) & 0b1111
    F = (x >> 30) & 0b11
    result = 0
    result |= E
    result |= B << 4
    result |= F << 6
    result |= A << 8
    result |= D << 23
    result |= C << 30
    return result

print(main(0x21eb958f))