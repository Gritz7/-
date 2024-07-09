First = int(input('First: '))
Second = int(input('Second: '))
Third = int(input('Third: '))
if First == Second == Third:
    print(3)
elif First == Second or Second == Third or First == Third:
    print(2)
else:
    print(0)
