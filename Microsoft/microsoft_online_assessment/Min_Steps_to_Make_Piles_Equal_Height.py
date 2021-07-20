'''
Alexa is given n piles of equal or unequal heights. In one step, Alexa can remove any number of boxes from the pile
which has the maximum height and try to make it equal to the one which is just lower than the maximum height of the stack.
Determine the minimum number of steps required to make all of the piles equal in height.

Example 1:

Input: piles = [5, 2, 1]
Output: 3
Explanation:
Step 1: reducing 5 -> 2 [2, 2, 1]
Step 2: reducing 2 -> 1 [2, 1, 1]
Step 3: reducing 2 -> 1 [1, 1, 1]
So final number of steps required is 3.

Input  : [1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
Output : 15
After sorting in reverse, we have...
[4, 4, 3, 3, 3, 2, 2, 2, 1] --> (2 steps to transform the 4's) --> The 3's must wait for 2 numbers before it to finish their reduction
[3, 3, 3, 3, 3, 2, 2, 2, 1] --> (5 steps to transform the 3's) --> The 2's must wait for 5 numbers before it to finish their reduction
[2, 2, 2, 2, 2, 2, 2, 2, 1] --> (8 steps to transform the 2's) --> The 1's must wait for 8 numbers before it to finish their reduction
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
'''

def min_steps_balance(piles):
    if not piles: return 0

    piles = sorted(piles, reverse=True)

    pre, count = piles[0], 0
    for i in range(len(piles)):
        if piles[i] != pre:
            count += i
            pre = piles[i]

    return count





if __name__ == '__main__':
    stacks = [
        [],
        [5, 2, 1],
        [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
        [50],
        [10, 10],
        [5, 2, 1],
        [4, 2, 1],
        [4, 5, 5, 4, 2],
        [4, 8, 16, 32],
        [4, 8, 8],
        [4, 4, 8, 8],
        [1, 2, 2, 3, 3, 4],
        [1, 1, 2, 2, 2, 3, 3, 3, 4, 4],
    ]

    answers = [
        0, 3, 15, 0, 0, 3, 3, 6, 6, 2, 2, 9, 15, 
    ]
    
    for stack, answer in zip(stacks, answers):
        res = min_steps_balance(stack)
        print("{} - [{}, {}]".format(res == answer, res, answer))

