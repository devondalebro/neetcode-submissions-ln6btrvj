class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res += str(len(string)) + '#' + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            str_len = int(s[i:j])
            i = j + 1
            string = s[i:i + str_len]
            i += str_len
            res.append(string)
        
        return res
        
