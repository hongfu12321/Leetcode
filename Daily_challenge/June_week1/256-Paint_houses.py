class Solution:
#     def minCost(self, costs: List[List[int]]) -> int:
    
#         def paint_cost(n, color):
#             if (n, color) in self.cache:
#                 return self.cache[(n, color)]

#             total_cost = costs[n][color]
#             if n == len(costs) - 1:
#                 pass
#             elif color == 0: # Red
#                 total_cost += min(paint_cost(n + 1, 1), paint_cost(n + 1, 2))
#             elif color == 1: # Green
#                 total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 2))
#             elif color == 2: # Blue
#                 total_cost += min(paint_cost(n + 1, 0), paint_cost(n + 1, 1))
#             self.cache[(n, color)] = total_cost
#             return total_cost
        
#         if costs == []: return 0
        
#         self.cache = {}
#         return min(paint_cost(0, 0), paint_cost(0, 1), paint_cost(0, 2))
    
    def minCost(self, costs: List[List[int]]) -> int:    
        for n in reversed(range(len(costs) - 1)):
            # Total cost of painting nth house red.
            costs[n][0] += min(costs[n + 1][1], costs[n + 1][2])
            # Total cost of painting nth house green.
            costs[n][1] += min(costs[n + 1][0], costs[n + 1][2])
            # Total cost of painting nth house blue.
            costs[n][2] += min(costs[n + 1][0], costs[n + 1][1])

        if len(costs) == 0: return 0
        return min(costs[0]) # Return the minimum in the first row.