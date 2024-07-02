my_dict = {"Sergei": 2001, "Vika": 2003,"Alexei": 1997}
print(my_dict)
print(my_dict.get("Sergei"))
print(my_dict.get("Antonio"))
my_dict.update({"Viktor": 1979, "Petya": 2006})
new = my_dict.pop("Vika")
print(my_dict)
print(new)

my_set = {1, 2, 3, 5, 6, 7, 7, 8, 3, 3, "string", "none", "string"}
print(my_set)
my_set.update({95, 97, 99, 99})
my_set.remove(7)
print(my_set)
