random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]
int_dict={}
float_tup=()
str_list=[]

for item in random_list:
    if isinstance(item, int):
        satuan = item % 10
        puluhan = (item//10) % 10
        ratusan = item // 100
        int_dict[item] = {"satuan":satuan, "puluhan": puluhan, "ratusan": ratusan}
    elif isinstance(item, float):
        float_tup += (item,)
    elif isinstance(item, str):
        str_list.append(item)

print("Int Map: ", int_dict)
print("Float Tuple: ", float_tup)
print("String list: ", str_list)
