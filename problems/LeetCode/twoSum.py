class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        numMap = {}     # Create an empty dictionry 
        n = len(nums)   # Define length of list

        # Build the hash table - assign each key with position of value 
        for i in range(n):  
            numMap[nums[i]] = i

        # Find the complement, if x + y = Target
        # x: i and y: compliment -> Target = i + compliment 
        # => compliment(hash_value) = Target - i        
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return []

# Test the function
sol = Solution()
lst = [3,4,6,7,11]
target = 13

print(sol.twoSum(lst, target))