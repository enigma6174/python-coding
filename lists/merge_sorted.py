def merge_sorted_lists(list_1, list_2):
    """
    Merge two input lists (sorted) together.
    This is not the same as union of two sets. In union operation, duplicates are removed.

    Time complexity O(M+N)
    Space complexity O(M+N)

    where M and N are the lengths of the input lists.

    :param list_1: list
    A list of sorted numbers
    :param list_2: list
    A list of sorted integers
    :return: list
    A merged list of integers from list_1 and list_2
    """
    x = len(list_1)
    y = len(list_2)

    # Final list which combines list_1 and list_2
    buffer = []

    # Pointers to keep track of current elements of list_1 and list_2
    i = 0
    j = 0

    # Iterate over the lists till the end of the smaller list is reached
    while i < x and j < y:

        # If list_1 current element is smaller
        if list_1[i] < list_2[j]:
            buffer.append(list_1[i])
            i += 1

        # If list_2 current element is smaller
        elif list_1[i] > list_2[j]:
            buffer.append(list_2[j])
            j += 1

        # If both list_1 and list_2 current elements equal
        else:
            # Comment either append line to perform union operation in case of duplicates
            buffer.append(list_1[i])
            buffer.append(list_2[j])
            i += 1
            j += 1

    # Add remaining elements of larger array to buffer
    while i < x:
        buffer.append(list_1[i])
        i += 1
    while j < y:
        buffer.append(list_2[j])
        j += 1

    return buffer


a = [4, 4, 4, 4, 4, 4, 4]
b = [4, 4, 4, 4, 4, 4, 4]
merged = merge_sorted_lists(a, b)

print(f"a={a}")
print(f"b={b}")
print(f"merged={merged}")
