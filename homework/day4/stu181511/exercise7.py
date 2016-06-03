from TypeChecker import check_obj_type
from exercise5 import get_first_two


@check_obj_type((dict,))
def parse_dict_vale(arg_dic):
    for k in arg_dic:
        arg_dic[k] = get_first_two(arg_dic[k])
    return arg_dic


@check_obj_type((dict,))
def parse_dict_vale2(arg_dic):
    return {k:get_first_two(v) for k, v in arg_dic.items()}


if __name__ == '__main__':
    print(parse_dict_vale({"k1": "v1v1", "k2": [11,22,33,44], "k3":[]}))
    print(parse_dict_vale2({"k1": "v1v1", "k2": [11, 22, 33, 44], "k3": []}))
