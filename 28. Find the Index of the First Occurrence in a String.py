class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - (k:=len(needle)) + 1):
            if haystack[i:i+k] == needle : return i
        return -1