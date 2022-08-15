from refactoring_220812.version2.define_properties import define_properties


# Split function to separate logic. Lowered code complexity.
def activate(region, env):
    region_timezone, city_name, threshold = define_properties(region, env)
    threshold = threshold + 10
    return region_timezone, city_name, threshold
