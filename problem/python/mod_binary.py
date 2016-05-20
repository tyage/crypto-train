def mod_binary(k, g, p):
    bin_format = "{0:b}".format(k)
    bin_k = []
    for i in range(0, len(bin_format)):
        bin_k.append(int(bin_format[len(bin_format) - 1 - i]))
    y = g
    for i in range(len(bin_k) - 2, -1, -1):
        if bin_k[i] == 1:
            y = ((y ** 2) % p) * g % p
        else:
            y = (y ** 2) % p
        print y
    return y

print mod_binary(730169,526032,1310723)
