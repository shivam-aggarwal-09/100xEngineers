# returning the sqaure of every element in a list

# function returning the squared list
def square(lst):
    return [i**2 for i in lst]

# creating a dynamic list
print("Input 5 elements space separated: ")
lst = map(int, input().split())
print(square(lst))