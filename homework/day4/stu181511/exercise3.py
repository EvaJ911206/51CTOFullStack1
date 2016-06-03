from TypeChecker import check_obj_type


@check_obj_type((str, list, tuple))
def count_len(obj):
    if len(obj) > 5:
        print('Length is larger than 5')
    else:
        print('Length is smaller than or equals to 5')


if __name__ == '__main__':
    count_len('aaaaa')
    count_len([1, 23, 4, 1, 2])
    count_len((1, 23, 4, 1, 2, '212', '11'))
