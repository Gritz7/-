immutable_var = 1, 2, 5, 7, False, True, "YO"
print(immutable_var)
#кортеж - неизменяемый элемент, он не поддерживает замену символов и элементов внутри себя
mutable_list = [1, 2, 5, 7, "YO", True, False]
mutable_list[0] = 77
mutable_list[-1] = "Global"
print(mutable_list)
