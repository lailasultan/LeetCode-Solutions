#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Kth Largest Element in Array
#LeetCode: Medium

#Given an integer array nums and an integer k, return the kth largest element in the array.

#Note that it is the kth largest element in the sorted order, not the kth distinct element.

#Can you solve it without sorting?


# In[ ]:


#Attempt 1s
import heapq

class Solution:
    def findKthLargest(self, nums, k):
        min_heap = nums[:k]           
        heapq.heapify(min_heap)        

        for num in nums[k:]:            
            if num > min_heap[0]:       
                heapq.heapreplace(min_heap, num) 

        return min_heap[0]  
#Time O(n logn) Space: O(n)

