class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans: List[int] = []
        nums_length = len(nums)

        ans = [*nums, *nums]
        return ans

            