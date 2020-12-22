# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one.
# Find that single one.
#
# Follow up: Could you implement a solution with a linear runtime complexity and without 
# using extra memory?
#
#
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
#
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
#
# Example 3:
# Input: nums = [1]
# Output: 1
#
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

# =================================================================================
# https://leetcode.com/problems/single-number/solution/
#
# Approach 3: Math
#
# Concept
# 2 * (a + b + c) - (a + a + b + b + c) = c2∗(a+b+c) − (a+a+b+b+c) = c
#
# Complexity Analysis
# * Time complexity : O(n + n) = O(n). sum will call next to iterate through nums. 
#   We can see it as sum(list(i, for i in nums)) which means the time complexity 
#   is O(n) because of the number of elements(n) in nums.
# * Space complexity : O(n + n) = O(n). set needs space for the elements in nums.
#

def singleNumber(nums: List[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    return 2 * sum(set(nums)) - sum(nums)

a = []
