class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstr = ""

        for i in range(min(len(word1), len(word2))):
            newstr += word1[i]
            newstr += word2[i]

        if len(word2) > len(word1):
            newstr += word2[len(word1):]
        
        else:
            newstr += word1[len(word2):]

        return newstr