# 1662. Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        if ''.join(word1) == ''.join(word2):
            return True
        else:
            return False

# 9. Palindrome Number
a = Solution()
a.arrayStringsAreEqual(["ab", "c"], ["a", "bc"])


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
        
x = Solution()
x.isPalindrome(121)