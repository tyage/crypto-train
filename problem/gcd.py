count = 0

def gcd(a, b):
    print b
    global count
    if b == 0:
        return a
    r = a % b
    count += 1
    return gcd(b, r)

print gcd( 341363, b = 255651)
