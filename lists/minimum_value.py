def find_min(arr):
    """
    Find the minimum element in array a
    Initialize the current_min to a[i] where i = 0
    Increment i and check if a[i] < current_min and replace if true

    Time complextiy O(N)

    :param arr: list
    A list of integers
    :return: int
    The minimum value in the list
    """

    i = 0
    current_min = arr[0]

    while i < len(arr):
        if arr[i] < current_min:
            current_min = arr[i]
        i += 1

    return current_min


lst = [9, 2, 3, 6, -99, 200, 67, 0]
res = find_min(lst)
print(res)
