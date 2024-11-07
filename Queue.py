#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Queue
#Leetcode: Easy

#You have a RecentCounter class which counts the number of recent requests within a certain time frame.

#Implement the RecentCounter class:

#RecentCounter() Initializes the counter with zero recent requests.
#int ping(int t) Adds a new request at time t, where t represents some time in milliseconds, and returns the number of requests that has happened in the past 3000 milliseconds (including the new request). Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
#It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


# In[ ]:


#Attempt 1
class RecentCounter(object):

    def __init__(self):
        self.queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.queue.append(t)
        count = 0
        maxLen = len(self.queue) -1
        for i in range(maxLen, -1, -1):
            val = self.queue[i]
            if val >= (t-3000) and val <= t:
                count += 1
            else:
                self.queue.pop(i)

        return count
#Time: O(n) Space: O(n)


# In[ ]:


#Attempt 2
from collections import deque

class RecentCounter(object):

    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """

        self.queue.append(t)
        
        while self.queue[0] < t-3000:
            self.queue.popleft()

        return len(self.queue)

#Time: O(1) Space: O(n)

