import heapq
import collections

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        d = defaultdict(int)
        for word in words:
            d[word] += 1
        
        ans = sorted(d.keys(), key = lambda x: (-d[x], x))
        return ans[:k]
        
