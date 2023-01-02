'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        def isCamelCase(string):
            return True if string == string[0].upper() + string[1:].lower() else False
        return True if word == word.upper() or word == word.lower() or isCamelCase(word) else False
'''

class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        lowercase = range(ord('a'), ord('z')+1)
        uppercase = range(ord('A'), ord('Z')+1)


        if ord(word[0]) in lowercase:
            for char in word:
                if ord(char) not in lowercase: return False
        
        else:
            word = word[1:]
            if not word: return True

            if ord(word[0]) in lowercase:
                for char in word:
                    if ord(char) not in lowercase: return False
        
            else:
                for char in word:
                    if ord(char) not in uppercase: return False
        
        return True




        