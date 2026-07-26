class Solution(object):
    def isAnagram(self, s, t):
        freq = {}
        freq1={}
        for i in s:
            if i in freq:
                freq[i] += 1
            else :
                freq[i] = 1
        for i in t:
            if i in freq1:
                freq1[i] += 1
            else :
                freq1[i] = 1
        if freq == freq1:
            return True
        else :
            return False