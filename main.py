# https://leetcode.com/explore/interview/card/top-interview-questions-easy/
# Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. 
# The remaining elements beyond index k - 1 can be ignored.
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function
class Solution:
    # Notice I moved nums inside the class logic to match how LeetCode calls it.
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case: if the array is empty, return 0
        if not nums:
            return 0
        
        # k keeps track of the index where the NEXT unique element should go.
        # We start at 1 because the first element (index 0) is always unique!
        k: int = 1 
        
        # We use a standard range loop starting at index 1
        for i in range(1, len(nums)):
            # If the current number is DIFFERENT from the previous number,
            # it's a new unique number!
            if nums[i] != nums[i - 1]:
                # Put this new unique number at position 'k'
                nums[k] = nums[i]
                # Increment k so the next unique number goes in the next slot
                k += 1
                
        return k

# Testing it locally
sol = Solution()
#my_nums = [1, 1, 2, 5]

my_nums = [0,0,1,1,1,2,2,3,3,4]

# LeetCode expects you to return the number of unique elements
unique_count = sol.removeDuplicates(my_nums)

print(f"Number of unique elements (k): {unique_count}")
print(f"Modified array: {my_nums}")
