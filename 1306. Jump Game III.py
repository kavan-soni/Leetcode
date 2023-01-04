class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        n = len(arr)
        q = [start]
        visited = set()

        while q:

            idx = q.pop()
            if arr[idx] == 0: return True
            
            if idx + arr[idx] not in visited and idx + arr[idx] < n : q.append(idx + arr[idx])
            if idx - arr[idx] not in visited and idx - arr[idx] > -1: q.append(idx - arr[idx])

            visited.add(idx)

        return False