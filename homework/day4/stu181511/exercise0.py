
def find_dict_diff(dic_old, dic_new):
    for k, v in dic_old.items():
        if k in dic_new:
            if isinstance(v, dict) and isinstance(dic_new[k], dict):
                find_dict_diff(v, dic_new[k])
            else:
                if v != dic_new[k]:
                    print("value %s is not in second dict, the second value is %s" % (v, dic_new[k]))
        else:
            print("key %s is not in second dict" % k)

if __name__ == '__main__':
    c1 = 1
    c2 = 2
    old_dict = {
        "#1": {'hostname': c1, 'cpu_count': 2, 'mem_capicity': 80},
        "#2": {'hostname': c1, 'cpu_count': 2, 'mem_capicity': 80},
        "#3": {'hostname': c1, 'cpu_count': 2, 'mem_capicity': 80}
    }

    new_dict = {
        "#1": {'hostname': c1, 'cpu_count': 2, 'mem_capicity': 800},
        "#3": {'hostname': c1, 'cpu_count': 2, 'mem_capicity': 80},
        "#4": {'hostname': c2, 'cpu_count': 2, 'mem_capicity': 80}
    }
    find_dict_diff(old_dict, new_dict)
    find_dict_diff(new_dict, old_dict)