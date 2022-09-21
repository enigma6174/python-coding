def rearrange1(lst):
    """
    Rearrange a list of sorted numbers where the first element is max 2nd is min 3rd is 2nd max ...
    Take two pointers i and j - front and back of array
    For every iteration add a[j] followed by a[i]
    Update both i and j till they cross over

    Time Complexity O(N)
    Space Complexity O(N)

    :param lst: List
    List of sorted numbers
    :return:
    List of rearranged numbers
    """
    i = 0
    j = len(lst) - 1
    buffer = []

    while i <= j:
        if i == j:
            buffer.append(lst[i])
        else:
            buffer.append(lst[j])
            buffer.append(lst[i])
        i += 1
        j -= 1

    return buffer


arr = [1, 2, 3, 4, 5]
res = rearrange1(arr)
print(res)
