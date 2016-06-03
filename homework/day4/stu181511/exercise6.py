from TypeChecker import check_obj_type


@check_obj_type((list, tuple))
def get_odd_element(arg):
    return arg[::2]


@check_obj_type((list, tuple))
def get_odd_element2(arg):
    rst = list()
    for i, v in enumerate(arg):
        if not i % 2:
            rst.append(v)
    return rst


@check_obj_type((list, tuple))
def get_odd_element3(arg):
    return [v for i, v in enumerate(arg) if not i % 2]


if __name__ == '__main__':
    print(get_odd_element([]))
    print(get_odd_element([1]))
    print(get_odd_element([1, 23, 4, 1, 2]))
    print(get_odd_element((1, 23, 4, 1, 2, '212', '11')))

    print(get_odd_element2([]))
    print(get_odd_element2([1]))
    print(get_odd_element2([1, 23, 4, 1, 2]))
    print(get_odd_element2((1, 23, 4, 1, 2, '212', '11')))

    print(get_odd_element3([]))
    print(get_odd_element3([1]))
    print(get_odd_element3([1, 23, 4, 1, 2]))
    print(get_odd_element3((1, 23, 4, 1, 2, '212', '11')))