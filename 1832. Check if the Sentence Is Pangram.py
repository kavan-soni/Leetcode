class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        d = defaultdict(int)

        for char in sentence:
            d[char] +=1
        
        return True if len(d.items())==26 else False