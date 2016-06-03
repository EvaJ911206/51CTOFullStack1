

fabi_cache = dict()


def fabi(n):
    global fabi_cache
    if n < 1:
        return 0
    if n <= 2:
        return 1
    # using cache to speed up the function
    if n in fabi_cache:
        return fabi_cache[n]
    fabi_cache[n] = fabi(n - 1) + fabi(n - 2)
    return fabi_cache[n]


def fabi2(n):
    if n < 1:
        return 0
    i = a = b = 1
    while i < n:
        a, b = b, a + b
        i += 1
    return a


if __name__ == '__main__':
    # for i in range(10):
    #     print(fabi(i))
    # for i in range(10):
    #     print(fabi2(i))
    print(fabi(9))
    print(fabi2(9))
