def to_bin_array(k):
    bin_format = "{0:b}".format(k)
    bin_k = []
    for i in range(0, len(bin_format)):
        bin_k.append(int(bin_format[len(bin_format) - 1 - i]))
    return bin_k

def ex_mod_binary(k1, g1, k2, g2, p):
    # e.g. 6 -> [0, 1, 1]
    bin_k1 = to_bin_array(k1)
    bin_k2 = to_bin_array(k2)

    # zero padding
    n = max(len(bin_k1), len(bin_k2))
    bin_k1 = [bin_k1[i] if i < len(bin_k1) else 0 for i in range(0, n)]
    bin_k2 = [bin_k2[i] if i < len(bin_k2) else 0 for i in range(0, n)]

    g_table = [
        [1, g1],
        [g2, g1*g2]
    ]

    y = 1
    for i in range(n - 1, -1, -1):
        g = g_table[bin_k2[i]][bin_k1[i]]
        y = ((y ** 2) % p) * g % p
    return y

# e.g. pow(42, 2, 13) * pow(5, 4, 13) % 13
print ex_mod_binary(2, 42, 4, 5, 13)
