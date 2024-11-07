#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Determine if Two Strings Are Close
#LeetCode: Medium
#Two strings are considered close if you can attain one from the other using the following operations:

#Operation 1: Swap any two existing characters.
#For example, abcde -> aecdb
#Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)


# In[ ]:


class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """

        
        if (set(word1) != set(word2)):
            return False

        freq1 = Counter(word1).values()
        freq2 = Counter(word2).values()

        if sorted(freq1) != sorted(freq2):
            return False
        
        return True
#Time O(n logn) Space: O(1)

