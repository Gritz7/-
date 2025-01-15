phone_book = {"Sergey": 88005553535, "Alex": 89164842610}
print(phone_book)
print(phone_book.get("Sergey"))
print(phone_book.get("Fatima"))
phone_book.update({"Artur": 89159552525, "Alina": 89654823535})
print(phone_book)
a1 = phone_book.pop("Alex")
print(phone_book)
print(a1)

my_set = {2, 2, 3, 4, 2, 4, True, True, "append", "hello", "hello", "Hello"}
print(my_set)
my_set.update([5, 7, 9])
my_set.remove(7)
print(my_set)