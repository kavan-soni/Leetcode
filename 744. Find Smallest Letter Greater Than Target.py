class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if ord(target) >= ord(letters[-1]): return letters[0]

        l, r = 0, len(letters)-1

        def condition(x):
            return ord(letters[x]) > ord(target)
        
        while l < r:
            m = l+(r-l)//2
            if condition(m): r = m
            else: l = m + 1
        return letters[l]