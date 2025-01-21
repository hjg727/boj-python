str_list = list("+++++")

for i in range(len(str_list)):
    str_list[i] = "#"
    print("".join(str_list))
    str_list[i] = "+"