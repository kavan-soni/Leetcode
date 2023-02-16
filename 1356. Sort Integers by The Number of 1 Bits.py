class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def hamming_weight(num: int) -> int:
            weight = 0
            while num:
                weight += 1
                num &= num - 1
            return weight

        return sorted(arr, key=lambda x: (hamming_weight(x), x))
    
    