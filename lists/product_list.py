def multiply1(lst):
    """
    Brute force solution
    For every element of the array calculate the product of the rest

    Time Complexity O(N*2)

    :param lst: list
    A list of integers
    :return: list
    A list of integers
    """

    end = len(lst)
    i = 0
    j = 0
    buffer = []

    while i < end:
        j = 0
        prod = 1
        while j < end:
            if i != j:
                prod *= lst[j]
            j += 1
        buffer.append(prod)
        i += 1

    return buffer


def multiply2(lst):
    """
    Optimized solution
    Calculate the product of the array in the first pass
    Iterate over the array and for every item, divide the product by item

    Time Complexity O(N + N) ~ O(N)
    One pass over the list to calculate product - O(N)
    Another pass over the list to divide by every item - O(N)

    :param lst: list
    A list of integers
    :return: list
    A list of integers
    """

    buffer = []
    zero_count = 0

    prod = 1
    for item in lst:
        if item != 0:
            prod *= item
        if item == 0:
            zero_count += 1

    if zero_count == 0:
        i = 0
        while i < len(lst):
            buffer.append(prod // lst[i])
            i += 1

    elif zero_count == 1:
        i = 0
        while i < len(lst):
            if lst[i] != 0:
                buffer.append(0)
            elif lst[i] == 0:
                buffer.append(prod)
            i += 1

    else:
        i = 0
        while i < len(lst):
            buffer.append(0)
            i += 1

    return buffer


arr = [2, 4, 0, 5, 0]
res = multiply2(arr)
print(res)
