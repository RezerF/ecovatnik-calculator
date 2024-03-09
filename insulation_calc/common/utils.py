
def combine_dicts(*args):
    result_dict = {}
    for d in args:
        for key, value in d.items():
            result_dict[key] = result_dict.get(key, 0) + value
    return result_dict