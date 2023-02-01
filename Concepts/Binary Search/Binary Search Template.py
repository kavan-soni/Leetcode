class Solution:
    '''
    Requirement for binary search is -> the search space is monotonic (increasing or decreaing).

    Three important things in binary search:
        1. set correct boundaries
        2. design correct condition function
        3. return correct value
    '''
    def binary_search(array) -> int:

        def condition(value) -> bool:
            # check something here
            pass

        left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid): right = mid
            else: left = mid + 1
            
        return left # minimal value satisfying condition function