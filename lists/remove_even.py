def remove_even(lst):
    """
    Removes the even numbers from the list

    Time complexity O(N)
    Space complexity O(N)

    :param lst: list
    List of integers
    :return: list
    List without even numbers
    """
    buffer = [x for x in lst if x % 2 != 0]
    print(buffer)


my_list = [1, 2, 4, 5, 10, 6, 3]
print(f"original_list: {my_list}")
remove_even(my_list)
