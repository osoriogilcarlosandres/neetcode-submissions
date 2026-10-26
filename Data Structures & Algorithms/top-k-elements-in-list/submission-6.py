class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        listt = [[] for i in range(len(nums) + 1)]
        
        for j in nums:
            dic[j] = 1 + dic.get(j, 0)
        
        for h, v in dic.items():
            listt[v].append(h)

        res = []

        for i in range(len(listt)-1, 0, -1):
            for n in listt[i]:
                res.append(n)
                if len(res)==k:
                   
                    return res
