from first import generate_sequence as gs
from second import MD5

# initial initialisation
w = 64
r = 20
b = 16  # bytes

pass_word = input("Input pass phrase in English: ")
encrypt_key = MD5.hash(pass_word)
encrypt_bytes = int(encrypt_key, 16).to_bytes(b, "little")
value_four_vec = bytes([(i % 265) for i in gs(8)])

# tool functions
rotate_left = lambda x, n: (x << n) | (x >> (32 - n))
modular_add = lambda a, b: (a + b) % pow(2, 32)
xor = lambda a, b: (a ^ b)


# create keys
u = int(w / 8)
c = int(b / u)

# step 1
s_keys = [i for i in gs(r * 2 + 2)]
l_keys = []
for i in range(c):
    l_keys.append(0)
    for j in range(u):
        l_keys[i] += pow(2, 8 * j) * encrypt_bytes[i * u + j]
# step 2
s_keys[0] = int("B7E151628AED2A6B", 16)
q_w = int("9E3779B97F4A7C15", 16)
for i in range(1, r * 2 + 2, 1):
    s_keys[i] = s_keys[i] + q_w

# step 3
A = B = 0
i = j = 0
for s in range(1, max(c, 2 * r + 2) * 3):
    s_keys[i] = (s_keys[j] + A + B) << 3
    A = s_keys[i]
    i = (i + 1) % (2 * r + 2)
    l_keys[j] = ((l_keys[j] + A + B) << ((A + B) if (A + B) < 64 else 64))
    B = l_keys[j]
    j = (j + 1) % c

# encryption
A = bytes("hey ", encoding="ascii")
print(int.from_bytes(bytearray, "little"))
B = "you!"


