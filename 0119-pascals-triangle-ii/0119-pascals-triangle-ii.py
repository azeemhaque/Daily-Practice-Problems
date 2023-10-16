class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = []
        start = 1
        result.append(start)
        for i in range(rowIndex):
            start = start * (rowIndex - i)
            start = start // (i + 1)
            result.append(start)
        return result