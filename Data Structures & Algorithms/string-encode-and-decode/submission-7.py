class Solution:

    def encode(self, strs: List[str]) -> str:
        retval = ''
        for word in strs:
            retval += str(len(word)) + '#' + word
        
        return retval


    def decode(self, s: str) -> List[str]:
        retStrs = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])

            j += 1
            end = j + length
            word = s[j : end]
            print(word)
            i = end
            
            retStrs.append(word)

        return retStrs
        

