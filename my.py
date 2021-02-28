print('Hello, World')
i = 1
while i < 7:
    j = 1
    while j < 7:
        print("%4d" % (i * j), end='')
        j += 1
    print()
    i += 1
    