class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:

        def binary_search(num):
            l, r = 0, n
            while l < r:
                m = l + (r-l)//2
                if num <= potions[m] : r = m
                else: l = m + 1
            return n-l

        potions, n = sorted(potions), len(potions)
        return [binary_search(-(-success//spell)) for spell in spells]