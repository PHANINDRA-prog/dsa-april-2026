// TC : O(n)
// SC : O(n)
from collections import Counter

class Solution:
    def minWindow(self, s, t):

        target = Counter(t)
        window = {}

        required = len(target)
        formed = 0
        left = 0
        answer = ""
        min_length = float("inf")

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0) + 1

            if (s[right] in target and window[s[right]] == target[s[right]]):
                formed += 1
            
            while formed == required:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    answer = s[left:right+1]
                window[s[left]] -= 1

                if (s[left] in target and window[s[left]] < target[s[left]]):
                    formed -= 1
                left += 1
        return answer
