class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}     # Create an empty dictionry 
        n = len(nums)   # Define length of list

        # Build the hash table 
        for i in range(n):  # i sequence start from 0 -> given length of n
            numMap[nums[i]] = i

        # Find the complement: x + y = Target. For x = nums[i] and y = complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []

sol = Solution()
lst = [3,4,6,7,11]
target = 13
print(sol.twoSum(lst, target))