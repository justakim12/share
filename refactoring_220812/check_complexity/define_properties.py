from refactoring_220812.version4.config import get_properties


def define_properties(region, env):
    region_timezone = get_properties("region_timezone", region, env)
    city_name = get_properties("city_name", region, env)
    threshold = get_properties("threshold", region, env)
    return region_timezone, city_name, threshold
