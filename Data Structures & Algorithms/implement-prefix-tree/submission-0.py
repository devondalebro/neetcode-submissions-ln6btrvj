class PrefixTree:
    class Node:
        def __init__(self):
            self.alpha = [None] * 26
            self.endWord = False

    def __init__(self):
        self.alpha = self.Node()

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
            
        cur = self.alpha
        for c in word:
            if cur.alpha[ord(c) - ord('a')] is None:
                cur.alpha[ord(c) - ord('a')] = self.Node()
            cur = cur.alpha[ord(c) - ord('a')]
        
        cur.endWord = True

    def search(self, word: str) -> bool:
        cur = self.alpha
        for c in word:
            if cur.alpha[ord(c) - ord('a')] is None:
                return False
            cur = cur.alpha[ord(c) - ord('a')]
        
        return cur.endWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.alpha
        for c in prefix:
            if cur.alpha[ord(c) - ord('a')] is None:
                return False
            cur = cur.alpha[ord(c) - ord('a')]

        return True