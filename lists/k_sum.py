def ksum1(lst, k):
    """
    This is a brute force solution.
    We iterate over every element of lst and compare it with the remaining items
    The comparison is successful if we get the required sum

    Time complexity is O(N^2) and space complexity is O(1)

    :param lst: list
    A list of unsorted integers
    :param k: int
    The value to check for sum
    :return: list
    A list with two integers that add up to k
    """

    # Index to keep track of current element being compared
    idx = 0

    buffer = []

    for i in lst:
        for j in lst[idx:]:
            k_sum = i + j
            if k_sum == k:
                buffer.append(i)
                buffer.append(j)
        idx += 1

        if len(buffer) == 2:
            break

    return buffer


def ksum2(lst, k):
    """
    This is an optimised solution.
    We sort the array and maintain two pointers (i,j) at front and end of list a
    If a[i] + a[j] > k then decrement j else increment i
    If a[i] + a[j] = k return (a[i], a[j])

    Time complexity is O(N + N*log(N)) and space complexity is O(1)
    O(N*log(N)) is the time for sorting and O(N) is the time to iterate over the list

    :param lst: list
    A list of unsorted integers
    :param k: int
    The value to check for sum
    :return: list
    A list with two integers that add up to k
    """

    lst.sort()

    i = 0
    j = len(lst) - 1

    while i < j:
        if lst[i] + lst[j] < k:
            i += 1
        elif lst[i] + lst[j] > k:
            j -= 1
        else:
            return [lst[i], lst[j]]

    return []


numbers = [1, 21, 3, 14, 5, 60, 7, 6]
target = 25

result = ksum2(numbers, target)
print(result)
