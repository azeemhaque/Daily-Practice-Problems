class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        low = min(salary)
        high = max(salary)
        salary.remove(low)
        salary.remove(high)
        for i in range(0, len(salary)):
            if(len(salary)==1):
                return(salary[i])
            else:
                sizesalary = float(len(salary))
                average = sum(salary)/sizesalary
                return(round(average,5))