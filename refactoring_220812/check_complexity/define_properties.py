def define_properties(region, env):
    if region == "kr":
        if env == "qa":
            region_timezone = "KST"
            city_name = "Seoul"
            threshold = 10
        elif env == "prod":
            region_timezone = "KST"
            city_name = "Busan"
            threshold = 10
    elif region == "jp":
        if env == "qa":
            region_timezone = "JST"
            city_name = "Tokyo"
            threshold = 40
        elif env == "prod":
            region_timezone = "JST"
            city_name = "Tokyo"
            threshold = 20
    elif region == "usa":
        if env == "qa":
            region_timezone = "PST"
            city_name = "San Francisco"
            threshold = 20
        elif env == "prod":
            region_timezone = "PST"
            city_name = "San Francisco"
            threshold = 20
    return region_timezone, city_name, threshold
