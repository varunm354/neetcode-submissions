class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        n = []
        heapq.heapify(nums)
        for i in range(len(nums)):
            val = heapq.heappop(nums)
            n.append(val)
    
        return n

        