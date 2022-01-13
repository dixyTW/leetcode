#Trie Solution
class Trie:
    def __init__(self):
        self.t = defaultdict(Trie)
        self.isWord = False
    
    def insert(self, word):
        tree = self
        for c in word:
            tree = tree.t[c]
        tree.isWord = True
    
    def search(self, word, i, skip):
        tree = self
        res = False
        if i == len(word):
            return tree.isWord and skip
        if not skip:
            res |= tree.search(word, i+1, True)
        if word[i] in tree.t:
            tree = tree.t[word[i]]
            res |= tree.search(word, i+1, skip)
        
        return res
    

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        tree = Trie()
        ans = 0
        for word in startWords:
            tree.insert(sorted(word))
        for word in targetWords:
            ans += tree.search(sorted(word), 0, False)
        return ans

#bit mask 
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        seen = set()
        ans = 0
        for word in startWords:
            bit = 0
            for c in word:
                bit ^= (0x1 << (ord(c) - 97))
            seen.add(bit)
        
        for word in targetWords:
            bit = 0
            for c in word:
                bit ^= (0x1 << (ord(c) - 97))
            for c in word:
                newbit = bit ^ (0x1 << (ord(c) - 97))
                if newbit in seen:
                    ans += 1
                    break 
        return ans