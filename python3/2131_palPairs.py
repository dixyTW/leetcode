class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        dic = defaultdict(list)
        pairs = 0
        same = 0
        both = 0
        
        for word in words:
            key = word
            flipped = 0
            if key[0] > key[1]:
                key = word[1] + word[0]
                flipped = 1
            if key not in dic:
                dic[key] = [0,0]
            dic[key][flipped] += 1
        
        for key in dic:
            if key[0] == key[1]:
                same += dic[key][0]
                pairs += (dic[key][0]//2)*2
                both += (dic[key][0]//2)*2
            else:
                pairs += min(dic[key])*2
        extra = 2 if same != both else 0
        return pairs*2 + extra
            
            
#         N = len(words)
#         pairs = 0
#         same = 0
#         both = 0
#         used = set()
        
#         for i in range(N):
#             for j in range(i+1,N):
#                 if words[i][0] == words[j][1] and words[i][1] == words[j][0] and i not in used and j not in used:
#                     pairs += 2
#                     used.add(i)
#                     used.add(j)
                    
#         for i in range(N):
#             if words[i][0] == words[i][1]:
#                 if i in used:
#                     both += 1
#                 same += 1
#         extra = 2 if same != both else 0
#         return pairs*2 + extra