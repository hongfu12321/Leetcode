class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        
        # Sort nums
        nums = sorted(nums) # time complexity of sorting in O(nlogn)
        
        # loop to iterate element in the array, if element is consecutive to the previous, tmp_counter + 1
        # if element is not consecutive, update max_counter, and reset the count of consecutive sequence
        max_counter = tmp_counter = 1
        pre = nums[0]
        
        for i in range(1, len(nums)): # time complexity of for loop is O(n)
            if nums[i] == pre + 1:
                tmp_counter += 1
            elif nums[i] == pre:
                pass
            else:
                max_counter = max(max_counter, tmp_counter)
                tmp_counter = 1
                
            pre = nums[i]
            
        return max(tmp_counter, max_counter)
    
        # time complexity is dominated by sorting, so it is equal to O(nlogn)
        # Space complexity is O(1) or O(n) depends on how we sort the array
        
        '''
        Runtime: 176 ms, faster than 74.97% of Python3 online submissions for Longest Consecutive Sequence.
        Memory Usage: 22.8 MB, less than 67.30% of Python3 online submissions for Longest Consecutive Sequence.
        '''