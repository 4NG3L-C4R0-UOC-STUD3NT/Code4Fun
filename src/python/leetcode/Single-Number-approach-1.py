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
# Approach 1: List operation
# Algorithm
#
# Iterate over all the elements in \text{nums}nums
# If some number in \text{nums}nums is new to array, append it
# If some number is already in the array, remove it
#
# Complexity Analysis
# * Time complexity : O(n^2). We iterate through nums, taking O(n) time. We search 
#   the whole list to find whether there is duplicate number, taking O(n) time. 
#   Because search is in the for loop, so we have to multiply both time complexities
#   which is O(n^2).
# * Space complexity : O(n). We need a list of size nn to contain elements in nums.
#

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    no_duplicate_list = []
    for i in nums:
        if i not in no_duplicate_list:
            no_duplicate_list.append(i)
        else:
            no_duplicate_list.remove(i)
    return no_duplicate_list.pop()


a = []
