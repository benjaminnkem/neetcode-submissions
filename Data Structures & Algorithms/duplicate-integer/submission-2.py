class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = []
        for num in nums:
            if num in track:
                return True
                break
            else:
                track.append(num)
        return False