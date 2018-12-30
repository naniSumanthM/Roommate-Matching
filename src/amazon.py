location_tuple = [(3, 8), (4, 3), (1, 1), (6, 5), (2, 6)]


def get_nearest_location(tup_list, num_of_locations):

    temp_list = []
    temp_map = {}

    for x, y in tup_list:
        square_root = round((((x*x)+(y*y))**.5), 2)
        temp_map[x, y] = square_root

    # for key, value in sorted(temp_map.iteritems(), key=lambda (k, v): (v, k)):
    #     if len(temp_list) < num_of_locations:
    #         temp_list.append(key)

    return temp_list


get_nearest_location(location_tuple, 3)
