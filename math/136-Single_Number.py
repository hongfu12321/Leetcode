class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         dic = {}
        
#         for n in nums:
#             if n not in dic:
#                 dic[n] = 1
#             else:
#                 dic[n] += 1
                
#         for k, v in dic.items():
#             if v == 1:
#                 return k
            
#         return -1
        
        return 2 * sum(set(nums)) - sum(nums)