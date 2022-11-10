class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        def searchTrie(letters):
            for letter in letters:
                if letter in children:
                    children = children[letter]
                else: return False
            return True

        def addToTrie():
            #write here


        def isPresent(letters):

            if letters[0] in children: 
                return searchTrie(letters)
            else:
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        if board[i][j] == letters[0]: 
                            #add exhaustively
            return False
        
        children = {}
        return [word if isPresent(list(word)) for word in words]


