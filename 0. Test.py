import collections
class Solution:

    def solution(a, b, c, d):
        
        q = [(a,b)]

        visited = set()
        visited.add((a,b))

        while q:
            x, y = q.pop(0)

            if (x,y) == (c,d) : return True
            if x+y <=c and (x+y, y) not in visited: q.append((x+y, y)); visited.add((x+y, y));
            if x+y <=d and (x, x+y) not in visited: q.append((x, x+y)); visited.add((x, x+y));
        
        return False
        
        '''



        d = collections.defaultdict(bool)

        def helper(x,y):
            if (x,y) in d: return d[(x,y)]

            if x == c and y == d: return True

            temp = False
            if x+y <=c : temp |= helper(x+y, y)
            if x+y <=d : temp |= helper(x, x+y)

            d[(x,y)] = temp
            return temp
        
        return "Yes" if helper(a,b) else "No"
        '''


        


    if __name__ == "__main__":

        print(solution(1,1,1000,1000))
        print(solution(1,4,5,9))
        print(solution(1,2,3,6))
        
        