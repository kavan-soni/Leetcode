class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def helper(idx, k, last_char, last_char_count):

            if k<0: return float('inf')
            if idx ==len(s): return 0
            
            delete = helper(idx+1, k-1, last_char, last_char_count)
            
            if s[idx] == last_char:
                keep =  helper(idx+1, k, last_char, last_char_count +1)             
                if last_char_count in (1,9,99): 
                    keep += 1
            else:
                keep =  1+ helper(idx+1, k, s[idx], 1)

            return min(delete, keep)
            
        return helper(0, k, "", 0)