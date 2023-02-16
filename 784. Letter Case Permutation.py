class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        n, ans = len(s), []
        def helper(string, index):
            if index == n : ans.append(string); return

            if s[index].isdigit() : helper(string + s[index], index + 1)
            else: 
                helper(string + s[index].upper(), index + 1)
                helper(string + s[index].lower(), index + 1)
            
        helper("", 0)
        return ans