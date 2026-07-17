class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def second_max(stones: List[int]) -> int:
            first = second = float('-inf')
            for i in stones:
                if i > first:
                    second = first
                    first = i
                elif first >= i > second:
                    second = i
            return second

        while len(stones) > 1:
            max_w = max(stones)
            second_w = second_max(stones)
            
            stones.remove(max_w)
            stones.remove(second_w)

            if max_w != second_w :
                new_num = max_w - second_w
                stones.append(new_num)

        
        return stones[0] if stones else 0