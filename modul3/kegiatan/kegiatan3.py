def map_to_units_tens_hundreds(digit, place):
    return {place: int(digit)}


def is_integer(x):
    return isinstance(x, int)


def is_float(x):
    return isinstance(x, float)


def is_str(x):
    return isinstance(x, str)


random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
int_dict = {}
float_tup = tuple(filter(is_float, random_list))
str_list = list(filter(is_str, random_list))

for i in filter(is_integer, random_list):
    item_str = str(i)
    place_values = ["ratusan", "puluhan", "satuan"]
    i_dict = {}
    for j in map(map_to_units_tens_hundreds, item_str, place_values):
        i_dict.update(j)
    int_dict[i] = i_dict

print("Int Map: ", int_dict)
print("Float Tuple: ", float_tup)
print("String list: ", str_list)
