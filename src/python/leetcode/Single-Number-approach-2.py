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
# Approach 2: Hash Table
# Algorithm
#
# We use hash table to avoid the O(n)O(n) time required for searching the elements.
#
# Iterate through all elements in nums and set up key/value pair.
# Return the element which appeared only once.
#
# Complexity Analysis
# * Time complexity : O(n . 1) = O(n). Time complexity of for loop is O(n). Time
#   complexity of hash table(dictionary in python) operation pop is O(1).
# * Space complexity : O(n). The space required by hash_table is equal to the number
#   of elements in nums.


def singleNumber(nums: List[int]) -> int:
    hash_table = defaultdict(int)
    for i in nums:
        hash_table[i] += 1
    
    for i in hash_table:
        if hash_table[i] == 1:
            return i

a = []
