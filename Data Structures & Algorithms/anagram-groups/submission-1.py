class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for string in strs:
            c_list = [0] * 25

            for c in string:
                c_index = ord(c) - ord('a')
                c_list[c_index] += 1
            
            if tuple(c_list) in anagrams:
                anagrams[tuple(c_list)].append(string)
            else:
                anagrams[tuple(c_list)] = [string]

        res = []
        for anagram in anagrams:
            res.append(anagrams[anagram])
        
        return res
            
            