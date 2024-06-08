import urllib3
import yaml

URL_CFG_DATA = "https://drive.google.com/uc?export=download&id=1f3P8czIFI3k3mLrhLjGlXhWsMXOnttyy"  # data.yml
# URL_CFG_DATA = "https://drive.google.com/uc?export=download&id=16RYtNiwpCEe2knOZRVJdz5XhcCbN8hdh" # data_old.yml


class Struct:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)
        for key, value in self.__dict__.items():
            if isinstance(value, dict):
                self.__dict__[key] = Struct(**value)

    def get(self, key):
        try:
            value = self.__dict__[key]
        except KeyError:
            return None
        return value


def cfg(yml_data):
    """Configure from yaml configuration"""
    return Struct(**yaml.safe_load(yml_data))


def get_data_cfg():
    http = urllib3.PoolManager()
    res = http.request('GET', URL_CFG_DATA)
    data = res.data.decode('utf-8')
    cfg_data = cfg(yml_data=data)
    print("Спарсил данные с диска!!")
    return cfg_data


def combine_dicts(*args):
    result_dict = {}
    for d in args:
        for key, value in d.items():
            result_dict[key] = result_dict.get(key, 0) + value
    return result_dict