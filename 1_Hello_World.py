# returning the sqaure of every element in a list

# function returning the squared list
def square(lst):
    return [i**2 for i in lst]


lst = [1,2,3,4,5]
print(square(lst))