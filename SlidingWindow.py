#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Sliding Window Problem
#Leetcode: Easy
#You are given an integer array nums consisting of n elements, and an integer k.

#Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


# In[ ]:


#Attempt 1
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        avg = -10000

        for i in range(len(nums)):
            if len(nums[i: k + i]) < k :
                break
            curr = float(sum(nums[i: k + i])) / k
            if curr > avg:
                avg = curr
        
        return avg
#Time: O(n^2) , Space: O(n), Result: Time Exceeded


# In[ ]:


#Attempt 2 
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        curr = maxsum = float(sum(nums[:k]))
        maxv = len(nums)
        if maxv == k:
            return curr / k
        for i in range(1, maxv-k+ 1):
            if k + i > maxv:
                break
            curr = float(curr - nums[i-1] + nums[k+i-1])
            if curr > maxsum:
                maxsum = curr
        
        return maxsum / k
#Time: O(n) Space: O(1)

