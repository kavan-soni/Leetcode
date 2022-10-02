class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        count = 0
        for n1 in arr1:
            flag = False
            for n2 in arr2:
                if abs(n1-n2)<=d:
                    flag = True
                    break
            
            if not flag:
                count +=1
        return count