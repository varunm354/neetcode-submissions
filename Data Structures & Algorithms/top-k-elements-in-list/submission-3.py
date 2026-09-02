class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        pairs = []
        res = []

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for num, freq in counts.items():
            pairs.append([freq, num])

        pairs.sort()

        for i in range(len(pairs) - 1, -1, -1):
            res.append(pairs[i][1])
            if len(res) == k:
                return res


        



          


        





        
        
