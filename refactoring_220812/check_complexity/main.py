from refactoring_220812.version4.define_properties import define_properties


# Split the dictionary into different yaml files to decrease code complexity
# and provide higher scalability.
def activate(region, env):
    region_timezone, city_name, threshold = define_properties(region, env)
    threshold = threshold + 10
    return region_timezone, city_name, threshold
