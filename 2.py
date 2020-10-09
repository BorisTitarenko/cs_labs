from bitarray import bitarray


def to_bit_array(string):
    bits = bitarray(endian='little')
    bits.frombytes(string.encode('utf-8'))
    return bits


def add_extension(bits):
    bits.append(1)
    needed_zeros = 448 - len(bits) % 512
    bits.extend(needed_zeros * bitarray('0'))
    return bits


def add_len(bits, strlen):
    ba = bitarray(endian='little')
    ba.frombytes(strlen.to_bytes(strlen.bit_length() // 8 + 1, byteorder='little'))
    print(ba)
    bits.extend(ba[:64])
    return bits



T = [
        0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
        0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
        0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x2441453, 0xd8a1e681, 0xe7d3fbc8,
        0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
        0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
        0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
        0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
    ]




def f_f(b, c, d):
    return (b & c) | (~b & d)


def f_g(b, c, d):
    return (b & d) | (c & ~d)


def f_h(b, c, d):
    return b ^ c ^ d


def f_i(c, b, d):
    return c ^ (b | ~d)


def lcshift(lst, s):
    return lst[s::] + lst[:s:]


def hex(bits):
    block_arr = [bits[i:(i+512)] for i in range(0, len(bits), 512)]
    first_circle_shifts = [7, 12, 17, 22]
    second_circle_shifts = [5, 9, 14, 20]
    third_circle_shifts = [4, 11, 16, 23]
    forth_circle_shifts = [6, 10, 15, 21]
    A = bitarray()
    B = bitarray()
    C = bitarray()
    D = bitarray()
    A.frombytes((0x67452301).to_bytes(4, "little"))
    B.frombytes((0xEFCDAB89).to_bytes(4, "little"))
    C.frombytes((0x98BADCFE).to_bytes(4, "little"))
    D.frombytes((0x10325476).to_bytes(4, "little"))
    md_buff = [A, B, C, D]
    for block in block_arr:
        word_arr = [block[j:(j + 32)] for j in range(0, 512, 32)]
        for i in range(16):
            
            md_buff[0] = (md_buff[1] + lcshift((md_buff[0] + f_f(md_buff[1], md_buff[2], md_buff[3])
                                                + word_arr[i] + T[i]) % 2 ** 32), 7) % 2 ** 32
            lcshift(md_buff, 1)
            md_buff[0] = (md_buff[1] + lcshift((md_buff[0] + f_f(md_buff[1], md_buff[2], md_buff[3])
                                                + word_arr[i] + T[i]) % 2 ** 32), 12) % 2 ** 32
            lcshift(md_buff, 1)
            md_buff[0] = (md_buff[1] + lcshift((md_buff[0] + f_f(md_buff[1], md_buff[2], md_buff[3])
                                                + word_arr[i] + T[i]) % 2 ** 32), 17) % 2 ** 32
            lcshift(md_buff, 1)
            md_buff[0] = (md_buff[1] + lcshift((md_buff[0] + f_f(md_buff[1], md_buff[2], md_buff[3])
                                                + word_arr[i] + T[i]) % 2 ** 32), 22) % 2 ** 32
            lcshift(md_buff, 1)


b = bitarray(endian="little")
c = bitarray(endian="little")
print(b)
print(0x67452301.to_bytes(4, "little"))
b.frombytes(0x67452301.to_bytes(4, "little"))
c.frombytes(0xEFCDAB89.to_bytes(4, "little"))
print(b)
print(c)
b.tobytes()
print(len(b + c))