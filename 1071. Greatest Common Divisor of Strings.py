class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        base = str1

        l1, l2 = len(str1), len(str2)

        def valid(base):
            n = len(base)
            if l1%n !=0 or l2%n !=0: return False
            if (l1//n)* base != str1 or (l2//n) * base != str2: return False
            return True


        while base and not valid(base):
            base = base[:-1]
        return base
            








