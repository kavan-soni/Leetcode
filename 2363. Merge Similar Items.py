class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        d = collections.defaultdict(lambda : 0)

        for item in items1 + items2:
            d[item[0]] += item[1]
        
        return sorted(d.items())

            
