// TC : O(n)
// SC : O(n)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Optimzed Solution
        strs.sort() # We would sort them in dictonary order

        i = 0
        first_word = strs[0]
        last_word = strs[-1]
        final_string = ""
        while i < len(first_word) and i < len(last_word):
            if first_word[i] == last_word[i]:
                final_string += first_word[i]
                i += 1
            else:
                break
        return final_string