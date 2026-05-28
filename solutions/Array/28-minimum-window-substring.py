//TC : O(n)
//SC : O(n)

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_count = Counter(t)
        window_count = {}

        have = 0
        need = len(t_count)

        left = 0
        answer = ""

        for right in range(len(s)):

            char = s[right]

            window_count[char] = window_count.get(char, 0) + 1

            # Requirement satisfied
            if char in t_count and window_count[char] == t_count[char]:
                have += 1

            # Window valid
            while have == need:

                current_window = s[left:right+1]

                if answer == "" or len(current_window) < len(answer):
                    answer = current_window

                # Remove left character
                left_char = s[left]
                window_count[left_char] -= 1

                # Requirement broken
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    have -= 1

                left += 1

        return answer