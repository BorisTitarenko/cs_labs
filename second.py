# from bitarray import bitarray
#
# class SmartBitArray(bitarray):
#     def __add__(self, other):
#         sum_arr = SmartBitArray(endian='little')
#         if (isinstance(other, int)):
#             sum_arr.frombytes(((int.from_bytes(self.tobytes(), 'little')
#                                 + other) % (2 ** 32)).to_bytes(4, 'little'))
#         else:
#             sum_arr.frombytes(((int.from_bytes(self.tobytes(), 'little')
#                               + int.from_bytes(other.tobytes(), 'little')) % (2 ** 32)).to_bytes(4, 'little'))
#         return sum_arr
#
# def to_bit_array(string):
#     bits = SmartBitArray(endian='little')
#     bits.frombytes(string.encode('utf-8'))
#     return bits
#
#
# def add_extension(bits):
#     bits.append(1)
#     needed_zeros = 448 - len(bits) % 512
#     bits.extend(needed_zeros * bitarray('0'))
#     return bits
#
#
# def add_len(bits, strlen):
#     ba = SmartBitArray(64, endian='little')
#     ba.setall(False)
#     ba.frombytes(strlen.to_bytes(strlen.bit_length() // 8 + 1, byteorder='little'))
#     bits.extend(ba[:64])
#     print(bits)
#     return bits
#
#
#
# T = [
#         0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
#         0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
#         0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 0xd62f105d, 0x2441453, 0xd8a1e681, 0xe7d3fbc8,
#         0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
#         0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
#         0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x4881d05, 0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
#         0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
#         0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391
#     ]
#
#
#
#
# def f_f(b, c, d):
#     return (b & c) | (~b & d)
#
#
# def f_g(b, c, d):
#     return (b & d) | (c & ~d)
#
#
# def f_h(b, c, d):
#     return b ^ c ^ d
#
#
# def f_i(c, b, d):
#     return c ^ (b | ~d)
#
#
# def lcshift(lst, s):
#     for i in range(s):
#         lst.insert(0, lst.pop())
#     return lst
#
# def rcshift(lst, s):
#     for i in range(s):
#         pass
#
# def hex(bits):
#     block_arr = [bits[i:(i+512)] for i in range(0, len(bits), 512)]
#     A = SmartBitArray(endian="little")
#     B = SmartBitArray(endian="little")
#     C = SmartBitArray(endian="little")
#     D = SmartBitArray(endian="little")
#     A.frombytes((0x67452301).to_bytes(4, "little"))
#     B.frombytes((0xEFCDAB89).to_bytes(4, "little"))
#     C.frombytes((0x98BADCFE).to_bytes(4, "little"))
#     D.frombytes((0x10325476).to_bytes(4, "little"))
#     md_buff = [A, B, C, D]
#     s_arr = [7, 12, 17, 22, 5, 9, 14, 20, 4, 11, 16, 23, 6, 10, 15, 21]
#     f_arr = [f_f, f_g, f_h, f_i]
#     for block in block_arr:
#         word_arr = [block[j:(j + 32)] for j in range(0, 512, 32)]
#         for c in range(4):
#             fun = f_arr[c % 4]
#             for i in range(16):
#                 k = i
#                 if(c == 1):
#                     k = (i + 5 * i) % 16
#                 elif(c == 2):
#                     k = (5 + 3 * i) % 16
#                 elif(c == 3):
#                     k = (7 * i) % 16
#                 md_buff[0] = md_buff[1] + lcshift((md_buff[0] + fun(md_buff[1], md_buff[2], md_buff[3])
#                                                    + word_arr[k] + T[c * 4 + i]), s_arr[c * 4 + i % 4])
#                 lcshift(md_buff, 1)
#     return md_buff
#
# buf = hex(add_len(add_extension(to_bit_array("")), 0))
# answer = buf[0] + buf[1] + buf[2] + buf[3]
# print(answer)

import struct
from enum import Enum
from math import (
    floor,
    sin,
)

from bitarray import bitarray


class MD5Buffer(Enum):
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476


class MD5(object):
    _string = None
    _buffers = {
        MD5Buffer.A: None,
        MD5Buffer.B: None,
        MD5Buffer.C: None,
        MD5Buffer.D: None,
    }

    @classmethod
    def hash(cls, string):
        cls._string = string

        preprocessed_bit_array = cls._step_2(cls._step_1())
        cls._step_3()
        cls._step_4(preprocessed_bit_array)
        return cls._step_5()

    @classmethod
    def _step_1(cls):
        bit_array = bitarray(endian="big")
        bit_array.frombytes(cls._string.encode("utf-8"))
        bit_array.append(1)
        while len(bit_array) % 512 != 448:
            bit_array.append(0)

        return bitarray(bit_array, endian="little")

    @classmethod
    def _step_2(cls, step_1_result):
        length = (len(cls._string) * 8) % pow(2, 64)
        length_bit_array = bitarray(endian="little")
        length_bit_array.frombytes(struct.pack("<Q", length))

        result = step_1_result.copy()
        result.extend(length_bit_array)
        return result

    @classmethod
    def _step_3(cls):
        for buffer_type in cls._buffers.keys():
            cls._buffers[buffer_type] = buffer_type.value

    @classmethod
    def _step_4(cls, step_2_result):
        F = lambda x, y, z: (x & y) | (~x & z)
        G = lambda x, y, z: (x & z) | (y & ~z)
        H = lambda x, y, z: x ^ y ^ z
        I = lambda x, y, z: y ^ (x | ~z)

        rotate_left = lambda x, n: (x << n) | (x >> (32 - n))

        modular_add = lambda a, b: (a + b) % pow(2, 32)

        T = [floor(pow(2, 32) * abs(sin(i + 1))) for i in range(64)]


        N = len(step_2_result) // 32

        for chunk_index in range(N // 16):
            start = chunk_index * 512
            X = [step_2_result[start + (x * 32) : start + (x * 32) + 32] for x in range(16)]

            X = [int.from_bytes(word.tobytes(), byteorder="little") for word in X]

            A = cls._buffers[MD5Buffer.A]
            B = cls._buffers[MD5Buffer.B]
            C = cls._buffers[MD5Buffer.C]
            D = cls._buffers[MD5Buffer.D]

            for i in range(4 * 16):
                if 0 <= i <= 15:
                    k = i
                    s = [7, 12, 17, 22]
                    temp = F(B, C, D)
                elif 16 <= i <= 31:
                    k = ((5 * i) + 1) % 16
                    s = [5, 9, 14, 20]
                    temp = G(B, C, D)
                elif 32 <= i <= 47:
                    k = ((3 * i) + 5) % 16
                    s = [4, 11, 16, 23]
                    temp = H(B, C, D)
                elif 48 <= i <= 63:
                    k = (7 * i) % 16
                    s = [6, 10, 15, 21]
                    temp = I(B, C, D)


                temp = modular_add(temp, X[k])
                temp = modular_add(temp, T[i])
                temp = modular_add(temp, A)
                temp = rotate_left(temp, s[i % 4])
                temp = modular_add(temp, B)

                A = D
                D = C
                C = B
                B = temp

            cls._buffers[MD5Buffer.A] = modular_add(cls._buffers[MD5Buffer.A], A)
            cls._buffers[MD5Buffer.B] = modular_add(cls._buffers[MD5Buffer.B], B)
            cls._buffers[MD5Buffer.C] = modular_add(cls._buffers[MD5Buffer.C], C)
            cls._buffers[MD5Buffer.D] = modular_add(cls._buffers[MD5Buffer.D], D)

    @classmethod
    def _step_5(cls):
        A = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.A]))[0]
        B = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.B]))[0]
        C = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.C]))[0]
        D = struct.unpack("<I", struct.pack(">I", cls._buffers[MD5Buffer.D]))[0]

        return f"{format(A, '08x')}{format(B, '08x')}{format(C, '08x')}{format(D, '08x')}"

if __name__ == "__main__":
    print(MD5.hash(""))
    print(MD5.hash("a"))