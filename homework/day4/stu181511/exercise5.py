from TypeChecker import check_obj_type


@check_obj_type((list, tuple, str))
def get_first_two(arg):
    return arg[:2]


@check_obj_type((list, tuple))
def get_first_two2(arg):
    # tuple can't be changed
    # so we need to change it to list
    arg = list(arg)
    del arg[2:]
    return arg


if __name__ == '__main__':
    print(get_first_two([1, 23, 4, 1, 2]))
    print(get_first_two((1, 23, 4, 1, 2, '212', '11')))

    print(get_first_two2([1, 23, 4, 1, 2]))
    print(get_first_two2((1, 23, 4, 1, 2, '212', '11')))
    print(get_first_two2([1]))
    print(get_first_two2([]))
