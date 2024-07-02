immutable_var = 1, 2, 3, "diamond", True
print(immutable_var)
#кортеж нельзя поменять тк он является неизменяемым эл-том, можно поменять только список внутри кортежа
mutable_list = ([1, 2, 3], "diamond", True)
mutable_list[0][2] = "hello"
mutable_list[0][0] = 5
print(mutable_list)
