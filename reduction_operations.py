class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort(reverse=True)  # Sort the array in descending order
        operations = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                operations += i
        return operations