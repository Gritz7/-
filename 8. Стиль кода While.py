my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while x < len(my_list):
    number = my_list[x]
    if number > 0:
        print(number)
    else:
        break
    x += 1
