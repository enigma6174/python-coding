def find_second_max1(lst):
    """
    Sort the array and return the element at index 1
    This approach will fail if we need to return the index
    This approach will fail if there were duplicates in the list

    Time Complexity is O(N*log(N))

    :param lst: List
    A list of numbers
    :return: int
    The second largest integer in the list
    """
    buffer = lst[:]
    buffer.sort(reverse=True)

    if len(buffer) > 1:
        return buffer[1]


def find_second_max2(lst):
    """
    Take two passes through the array
    In the first pass calculate the max and record the value
    Copy all elements except those that are max into new array
    In the second pass calculate the max and this will be the second max

    This approach will work if there are duplicates in the list

    Time complexity is O(N)

    :param lst: List
    List of numbers
    :return: int
    Second largest number in the list
    """
    current_max = lst[0]
    buffer = []

    # First pass - calculate the max of the array
    i = 0
    while i < len(lst):
        if lst[i] > current_max:
            current_max = lst[i]
        i += 1

    # Second pass - copy elements to new array except max
    i = 0
    while i < len(lst):
        if lst[i] != current_max:
            buffer.append(lst[i])
        i += 1

    # Third pass - find the max of new array
    i = 0
    current_max = buffer[0]
    while i < len(buffer):
        if buffer[i] > current_max:
            current_max = buffer[i]
        i += 1

    return current_max


arr = [4, 2, 4, 1]
res = find_second_max1(arr)
print(res)
