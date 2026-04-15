class WordDictionary:
    class Node:
        def __init__(self):
            self.alpha = [ None ] * 26
            self.endWord = False

    def __init__(self):
        self.alpha = self.Node()

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            return
            
        cur = self.alpha
        for c in word:
            if cur.alpha[ord(c) - ord('a')] is None:
                cur.alpha[ord(c) - ord('a')] = self.Node()
            cur = cur.alpha[ord(c) - ord('a')]
        
        cur.endWord = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            cur = node
            for (i, c) in enumerate(word):
                if c == '.':
                    for n in cur.alpha:
                        if n is None:
                            continue
    
                        if dfs(n, word[i + 1:]) is True:
                            return True
                    return False
                else:
                    if cur.alpha[ord(c) - ord('a')] is None:
                        return False
                    cur = cur.alpha[ord(c) - ord('a')]
            
            return cur.endWord
        
        return dfs(self.alpha, word)
        
