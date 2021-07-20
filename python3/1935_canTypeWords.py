class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        tokens = text.split(" ")
        s = set()
        count = 0
        for c in brokenLetters:
            s.add(c)
        for token in tokens:
            ok = True
            for c in token:
                if c in s:
                    ok = False
                    break
            if ok:
                count += 1
        return count