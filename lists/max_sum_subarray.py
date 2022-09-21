def sum1(lst):
    """
    Simple brute force solution is to calculate the sum of the subarray for every element in the array
    Update the current sum if the calculated sum is more
    Keep tracking the sum using a global sum variable

    Time complexity O(N*2)

    :param lst: List
     An array of positive and negative integers
    :return: int
    The maximum sum of the subarray
    """
    max_sum = float("-inf")

    for i in range(len(lst)):

        _sum = 0
        current_max = 0

        for j in range(i, len(lst)):
            _sum += lst[j]
            if _sum > current_max:
                current_max = _sum

        if current_max > max_sum:
            max_sum = current_max

    return max_sum


arr = [-2, -5, 6, -2, -3, 1, 5, -6]
res = sum1(arr)
print(res)
