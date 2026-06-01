// TC : O(n*m)
// SC : O(1)
# Brute Force Approach

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         first_word = strs[0]
#         answer = ""
#         for index,char in enumerate(first_word):
#             count = 0
#             valid = False
#             for word in strs:
#                 if index < len(word) and word[index] == char:
#                     count += 1
#                     valid = True
#                 else:
#                     valid = False
#                     break
#             if not valid:
#                 break
#             if count == len(strs):
#                 answer += char
#         return(answer)

class Solution:
    def longestCommonPrefix(self, strs):

        prefix_length = 0

        for index, char in enumerate(strs[0]):

            for word in strs:

                if index >= len(word) or word[index] != char:
                    return strs[0][:prefix_length]

            prefix_length += 1

        return strs[0][:prefix_length]