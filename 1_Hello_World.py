# returning the sqaure of every element in a list

# function returning the squared list
def square(lst):
    return [i**2 for i in lst]

# Input the number of elements that you want in a list
lst_len = input("Enter the number of elements: ")

# User will enter the space separated elements
print("Input {} space separated integers".format(lst_len))
lst = list(map(int, input().split()))

# calling the function and prnting the output
print(square(lst))

