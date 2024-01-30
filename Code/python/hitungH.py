def H(u, v, w):
    return (2 * u * (v * v)) + (3 * v * w) + (10 * v)

bil1 = int(input("Bilangan 1: "))
bil2 = int(input("Bilangan 2: "))
bil3 = int(input("Bilangan 3: "))

print(H(bil1, bil2, bil3))