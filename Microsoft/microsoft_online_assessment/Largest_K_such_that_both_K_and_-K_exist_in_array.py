'''
Microsoft | OA 2019 | Largest K such that both K and -K exist in array

Write a function that, given an array A of N integers, returns the lagest integer K > 0 such that both values K and -K exist in array A. If there is no such integer, the function should return 0.

Example 1:

Input: [3, 2, -2, 5, -3]
Output: 3
Example 2:

Input: [1, 2, 3, -4]
Output: 0
'''

def get_largest_K(arr):
    if not arr: return 0

    arr = sorted(arr, reverse=True)
    left, right = 0, len(arr) - 1

    while left < right and arr[right] <= 0:
        if arr[left] > arr[right] * -1:
            left += 1
        elif arr[left] < arr[right] * -1:
            right -= 1
        else:
            return arr[left] 

    return 0




if __name__ == '__main__':
    stacks = [
        [3, 2, -2, 5, -3],
        [1, 2, 3, -4],
    ]

    answers = [
        3, 0
    ]
    
    for stack, answer in zip(stacks, answers):
        res = get_largest_K(stack)
        print("{} - [{}, {}]".format(res == answer, res, answer))


