// Time Complexity O(n)
// Space complexity O(26) which is O(1)
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for elem in strs:

            count = [0]*26

            for char in elem:
                index = ord(char) - ord('a')
                count[index] += 1
            

            key = tuple(count)
            anagram_map[key].append(elem)

        return list(anagram_map.values())


