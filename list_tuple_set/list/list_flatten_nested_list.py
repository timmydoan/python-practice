my_list = [1, 2, [3, 4], [5, [6, 7]], 8, [9, 10, [11, 12]]]

def flatten_nested_list(my_list):
    flattened_list = []
    for item in my_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_nested_list(item))
        else:
            flattened_list.append(item)
    return flattened_list