def define_properties(region, env):
    properties = {
        "kr":
            {"qa":
                 {"region_timezone": "KST",
                  "city_name": "Seoul",
                  "threshold": 10},
             "prod":
                 {"region_timezone": "KST",
                  "city_name": "Seoul",
                  "threshold": 10},
             },
        "jp":
            {"qa":
                 {"region_timezone": "JST",
                  "city_name": "Tokyo",
                  "threshold": 40},
             "prod":
                 {"region_timezone": "JST",
                  "city_name": "Tokyo",
                  "threshold": 20},
             },
        "us":
            {"qa":
                 {"region_timezone": "PST",
                  "city_name": "San Francisco",
                  "threshold": 20},
             "prod":
                 {"region_timezone": "PST",
                  "city_name": "San Francisco",
                  "threshold": 20},
             },
    }

    region_timezone = properties[region][env]["region_timezone"]
    city_name = properties[region][env]["city_name"]
    threshold = properties[region][env]["threshold"]

    return region_timezone, city_name, threshold
