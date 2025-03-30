primos = []
n = 2

while len(primos) < 100:
    if n < 2:
        primo = False
    elif n == 2:
        primo = True
    elif n % 2 == 0:
        primo = False
    else:
        primo = True
        i = 3
        while i * i <= n:
            if n % i == 0:
                primo = False
                break
            i += 2

    if primo:
        primos.append(n)
    n += 1

print(primos)
