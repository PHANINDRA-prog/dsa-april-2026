//TC : O(n)
//SC : O(1)

class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        s = ""
        
        # 1. Edge case handled
        if len(chars) == 1:
            return 1
            
        # 2. Build the compressed string correctly
        for right in range(len(chars)):
            if chars[left] != chars[right]:
                count = right - left
                # Only add the number if the count is greater than 1
                s += f"{chars[left]}{count if count > 1 else ''}"
                left = right
                
        # 3. Handle the very last group after the loop ends
        count = len(chars) - left
        s += f"{chars[left]}{count if count > 1 else ''}"
        
        # 4. Correctly overwrite the input array in-place
        for i in range(len(s)):
            chars[i] = s[i]

        # 5. You MUST return the length of the new compressed string, not 'chars'
        return len(s)

