def unique(lst):
    """
    Find the first unique element in the list.
    A unique element is a non-repeating element.
    For every element compare with all other elements for uniqueness
    If the element is unique add to new list and after all passes return first element of unique list
    This approach will give us access to fir k-unique elements also

    Time Complexity O(N*2) but in best case O(N) when one pass is enough

    :param lst: List
    A List of integers
    :return: int
    The first unique element in the list
    """

    i = 0
    uniques = []

    while i < len(lst):
        current_unique = lst[i]
        is_unique = True
        j = 0
        while j < len(lst):
            if lst[i] == lst[j] and i != j:
                is_unique = False
                break
            j += 1
        if is_unique:
            uniques.append(current_unique)
        i += 1

    if len(uniques) != 0:
        return uniques[0]


arr = [0, 0, 0, 4]
res = unique(arr)
print(res)
