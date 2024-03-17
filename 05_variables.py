# Lession 05: Variables.
# Variable is object for containing specific value like container.
# Variable is changable.
# Variable can store String, Integer, Float, Boolean etc.

x = 5
print(x)

y = "We are learning python"
print(y)

# Changing of Variable
x = 6
y = "Python is a programming language"
print(x)
print(y)

# If you want to specify the data type of a variable, this can be done with casting.
# type() To check the data type of a variable

print(type("I am learning python"))
print(type(2+2))
print(type(4.5))
print(type(True))

# Rule to assign a variable
# 1. The variable should contain letters, numbers or underscores
# 2. Do not start with numbers.
# 3. Spaces are not allowed
# 4. Do not use keywords used in function (break, mean, median, test etc.)
# 5. Short and descriptive.
# 6. Case sensitive (Lowercase, Uppercase, letters lower case letter should be used.)


# Multi Words Variable Names.
# Variable names with more than one word can be difficult to read.
# There are several techniques you can use to make them more readable:

# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"
