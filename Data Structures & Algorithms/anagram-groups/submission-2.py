class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for  v in strs:
            array = [0] * 26
            for i in v:
                array[ord(i) - ord("a")] += 1
            
            dic[tuple(array)].append(v)
        return list(dic.values())