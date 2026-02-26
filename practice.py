
numbers_list = [10, 36, 70, 49, 51]

max_num = numbers_list[0]

for i in numbers_list:

    if max_num < i:
        print(max_num, i)  # Debugging
        max_num = i
        print("Max Number is i =", i)  # Debugging

print(max_num)
