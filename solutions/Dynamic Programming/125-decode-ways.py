class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        

        def valid(num):
            if num[0] == "0":
                return False
            return 1<=int(num)<=26
        
        @cache
        def helper(i):
            if i == n:
                return 1
            
            total_ways = 0
            # Pick 1 digit
            if valid(s[i]):
                total_ways += helper(i + 1)
            
            # Pick 2 digit
            if i+2 <= n and valid(s[i:i+2]):
                total_ways += helper(i+2)
            
            return total_ways
        return helper(0)
            
