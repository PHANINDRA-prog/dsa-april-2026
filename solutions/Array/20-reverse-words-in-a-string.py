//TC : O(n)
//SC : O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        non_space = s.split()
        non_space[:] = non_space[::-1]
        final_string = " ".join(non_space)
        return(final_string)