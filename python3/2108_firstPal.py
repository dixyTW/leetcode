class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_pal(word):
            #helper to check if word is palindrome
            for i in range(len(word)//2):
                if word[i] != word[len(word)-1-i]:
                    return False
            return True
        for word in words:
            if is_pal(word):
                return word
        return ""