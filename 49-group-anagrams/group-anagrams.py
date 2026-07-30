class Solution(object):
    def groupAnagrams(self, strs):
        groups={}
        for i in strs:
            key="".join(sorted(i))
            if key in groups:
                groups[key].append(i)
            else:
                groups[key]=[i]
        result = list(groups.values())
        return result
        