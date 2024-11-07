#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Product of Array Except Self
#Leetcode: Medium

#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

#The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# In[ ]:


#Attempt 1

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            arr.append(1)
            for j in range(len(nums)):
                if i == j:
                    continue

                arr[i] *= nums[j]

        return arr
    
#Time O(n^2)  Space: O(n)


# In[ ]:


#Attempt 2

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        arr = [1] * n

        left_arr = 1
        for i in range(n):
            arr[i] = left_arr
            left_arr *= nums[i]
        print(arr)

        right_arr = 1
        for j in range(n-1, -1, -1):
            arr[j] *= right_arr
            right_arr *= nums[j]

        return arr
    
#Time: O(n) Space: O(n)

