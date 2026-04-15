class Solution:
    def isPalindrome(self, s: str) -> bool:
        pure_string = ""
        for c in s:
            if c.isalnum():
                print(c)
                pure_string += c.lower()
        
        i = 0
        while i < len(pure_string) // 2:
            if pure_string[i] != pure_string[len(pure_string) - i - 1]:
                return False
            i += 1

        return True
        
        
