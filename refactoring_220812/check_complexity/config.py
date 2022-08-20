import pathlib

import yaml


def get_properties(key, region, env):
    region = region
    env = env

    file_path = f"{pathlib.Path(__file__).parent.absolute()}/{region}/{env}/properties.yaml"
    with open(file_path) as file:
        properties = yaml.load(file.read(), Loader=yaml.FullLoader)
    return properties.get(key)
