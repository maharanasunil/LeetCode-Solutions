class Solution:
    def average(self, salary: List[int]) -> float:
        newSalary = sorted(salary)[1:-1]
        return sum(newSalary)/len(newSalary)