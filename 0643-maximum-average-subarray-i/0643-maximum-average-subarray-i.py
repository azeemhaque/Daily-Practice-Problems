class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = sum(nums[:k])
        
        max_sum = window_sum
        max_index = 0
        for i in range(k,n):
            window_sum = window_sum + nums[i] - nums[i-k]
            max_sum = max(max_sum,window_sum)
            
        return round((max_sum/k),5)