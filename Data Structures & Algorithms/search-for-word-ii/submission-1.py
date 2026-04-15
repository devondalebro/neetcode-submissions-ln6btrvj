class Solution:
    class TrieNode:
        def __init__(self):
            self.alpha = [ None ] * 26
            self.endWord = False
    
    def wordSearch(self, word, t, r, c, cellList):
        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        if t.alpha[ord(self.board[r][c]) - ord('a')] is None:
            return ''
        
        word += self.board[r][c]
        cellList.add(tuple([r, c]))
        t = t.alpha[ord(self.board[r][c]) - ord('a')]
        
        if t.endWord is True:
            self.ret.add(tuple(word))
        
        for i in range(4):
            rNew = r + dr[i]
            cNew = c + dc[i]
            if rNew < 0 or rNew >= len(self.board):
                continue
            if cNew < 0 or cNew >= len(self.board[0]):
                continue

            if tuple([rNew, cNew]) in cellList:
                continue
            
            if t.alpha[ord(self.board[rNew][cNew]) - ord('a')] is None:
                continue
            
            self.wordSearch(word, t, rNew, cNew, cellList)

        cellList.remove(tuple([r, c]))

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        alpha = self.TrieNode()
        
        for w in words:
            cur = alpha
            for c in w:
                if cur.alpha[ord(c) - ord('a')] is None:
                    cur.alpha[ord(c) - ord('a')] = self.TrieNode()
                cur = cur.alpha[ord(c) - ord('a')]
            cur.endWord = True
        
        self.ret = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.board[r][c] == '.':
                    continue

                if alpha.alpha[ord(self.board[r][c]) - ord('a')] is None:
                    continue
                
                self.wordSearch('', alpha, r, c, set())

        ret = []
        for w in self.ret:
            print(w[0])
            ret.append(''.join(w))
        return ret



                    
