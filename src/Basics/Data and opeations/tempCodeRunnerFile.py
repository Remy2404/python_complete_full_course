def custom_sum_list_with_length(mylist):
    return divmod(mylist) , len(mylist)

mylist = [1, 2, 3, 4, 5]
result, length= custom_sum_list_with_length(mylist)
print(f"The sum of the list {mylist} is {result}.")
print(f"The length of the list is {length}.")
