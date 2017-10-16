Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].



solution 1:
暴力搜索，双重循环遍历。时间复杂度 $O(n_{2})$，空间复杂度$O(1)$

solutin 2:
哈希表，差值求索引。时间复杂度 $O(n)$，空间复杂度$O(1)$