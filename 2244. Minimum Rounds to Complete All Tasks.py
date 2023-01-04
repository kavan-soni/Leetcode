class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        
        counter = collections.Counter(tasks)
        ans = 0

        for num in counter:

            if counter[num] == 1: return -1
            
            x = counter[num] % 6
            if x ==1 :
                counter[num] -= 7
                ans += 3
                ans += (counter[num]//3)
            if x == 0 or x == 3: ans += (counter[num]//3)
            if x == 2 or x == 5: ans += 1 + (counter[num]//3)
            if x == 4: ans += 2 + (counter[num]//6)*2

        return ans

