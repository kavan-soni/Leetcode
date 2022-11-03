class Solution:
    def longestPalindrome(self, words: List[str]) -> int: 

        d = collections.defaultdict(int)
        s = set()
        answer = 0

        for word in words:
            d[word] +=1
            s.add(word)
        oddLength = 0



        while d:
            print(d, answer+oddLength)
            word = next(iter(d.items()))[0]
            if word == word[::-1]:
                answer+= ((d[word]//2) * 2 * len(word))
                d[word] -= ((d[word]//2) * 2)
                if d[word]: oddLength = max(oddLength, d[word]*len(word))
                del(d[word])

            elif word[::-1] in s:
                answer += (2 * len(word) * min(d[word],d[word[::-1]]))
                del(d[word])
                del(d[word[::-1]])
            else: del(d[word])
        print(d, answer+oddLength)
        return answer+oddLength

            
                



                






        


