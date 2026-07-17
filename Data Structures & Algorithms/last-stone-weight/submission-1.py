import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # def second_max(stones: List[int]) -> int:
        #     first = second = float('-inf')
        #     for i in stones:
        #         if i > first:
        #             second = first
        #             first = i
        #         elif first >= i > second:
        #             second = i
        #     return second

        # while len(stones) > 1:
        #     max_w = max(stones)
        #     second_w = second_max(stones)
            
        #     stones.remove(max_w)
        #     stones.remove(second_w)

        #     if max_w != second_w :
        #         new_num = max_w - second_w
        #         stones.append(new_num)

        
        # return stones[0] if stones else 0
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, -(y-x))
        return -stones[0] if stones else 0
