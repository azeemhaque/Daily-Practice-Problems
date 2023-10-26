import numpy as np
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = np.concatenate((nums,nums))
        return ans