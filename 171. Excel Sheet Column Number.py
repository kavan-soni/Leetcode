class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        colnum = 0

        for i in range(-1,-len(columnTitle)-1,-1):
            colnum += (26**(-(i+1))) * (ord(columnTitle[i])-64)
        return colnum