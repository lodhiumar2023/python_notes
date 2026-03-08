# Recursive Function

def show(a):
    if a == 0:  # Base case
        return
    print(a)
    show(a-1)


show(5)
