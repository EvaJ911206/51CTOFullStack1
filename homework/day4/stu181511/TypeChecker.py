from functools import partial


def check_obj_type(types):
    def _deco(func):
        def _wrap(ipt_obj):
            f = partial(isinstance, ipt_obj)
            #f = lambda x: isinstance(ipt_obj, x)
            if any(map(f, types)):
                return func(ipt_obj)
            else:
                print('Wrong input type')
        return _wrap
    return _deco
