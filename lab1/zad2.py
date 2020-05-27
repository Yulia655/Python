def foo(num_list):
    for i in range(1, len(num_list)):
        if num_list[i] < num_list[i - 1]:
            return False
    return True


list_ = [2, 3, 4, 5, 7]
print(foo(list_))
list_ = [2, 3, 4, 5, 9]
print(foo(list_))

#Complete
