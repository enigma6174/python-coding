def rearrange1(lst):
    """
    A simple brute force solution is to sort the array

    Time complexity is O(N*log(N))
    Space complexity is O(N)

    :param lst: List
    A list of positive and negative integers
    :return: List
    A list where negative numbers come first followed by positive numbers
    """
    lst.sort()
    return lst


def rearrange2(lst):
    """
    A simple optimised solution is to have a new empty array and pass over the list two times
    In the first pass add all the negative numbers to the empty array
    In the second pass add the positive numbers to the above array

    Time Complexity is O(N)
    Space Complexity is O(N)

    :param lst: List
    A list of positive and negative integers
    :return: List
    A list where negative integers come first followed by positive integers
    """

    buffer = []

    i = 0
    while i < len(lst):
        if lst[i] < 0:
            buffer.append(lst[i])
        i += 1

    i = 0
    while i < len(lst):
        if lst[i] >= 0:
            buffer.append(lst[i])
        i += 1

    return buffer


arr = [10, -1, 20, 4, 5, -9, -6]
res = rearrange1(arr)
print(res)
