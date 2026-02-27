
data_list = [1, 2, 3, 4, 5, 6, 10, 7, 8, 9, 10, 10]

list_index = 0
x = 10

for i in data_list:
    if x == i:
        print(i)
        list_index = list_index + 1
print(list_index)