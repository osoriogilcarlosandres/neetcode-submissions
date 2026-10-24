class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dics = defaultdict(int)
        for i in nums:
            dics[i] += 1
        sorted_dic = dict(sorted(dics.items(), key=lambda item: item[1]))
        lis = list(sorted_dic.keys())
        liss=[]
        for i in range(k):
            liss.append(lis.pop())
        return liss
