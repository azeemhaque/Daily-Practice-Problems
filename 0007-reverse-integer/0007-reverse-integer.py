class Solution:
    def reverse(self, x: int) -> int:
        s = str(abs(x))[::-1]
        sign = -1 if x < 0 else 1
        rx = int(s) * sign
        return 0 if rx < -2**31 or rx > 2**31 - 1 else rx