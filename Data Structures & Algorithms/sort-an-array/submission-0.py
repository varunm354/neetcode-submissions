class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        newnums = []

        for i in range(len(nums)):
            val = min(nums)
            newnums.append(val)
            nums.remove(val)

        return newnums

        