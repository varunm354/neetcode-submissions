class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, val in count.items():
            if val > (len(nums) / 3):
                res.append(key)
        return res

        