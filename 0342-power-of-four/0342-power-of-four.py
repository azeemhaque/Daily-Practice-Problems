class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        true = True
        false = False
        for i in range(16):
            power = 4**i
            
            if(power == n):
                return true
            if(power > n):
                return false
        return false