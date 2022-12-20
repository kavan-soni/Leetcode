class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = set()

        def helper(room):
            if room<0 or room >= n or room in visited : return
            visited.add(room)
            for key in rooms[room]:
                helper(key)

        helper(0)
        return len(visited) == n