# DSA Problems Solutions

## Progress
**Solved:** 6/145 problems  
**Last Updated:** May 24, 2026

## Solutions

| # | Problem | Difficulty | LeetCode | Solution | Date Solved | Notes |
|---|---------|-----------|----------|----------|-------------|-------|
| 1 | Two Sum | Easy | [Link](https://leetcode.com/problems/two-sum/) | [Code](https://raw.githubusercontent.com/PHANINDRA-prog/dsa-april-2026/main/solutions/Array/1-two-sum.py?raw=true) | May 17, 2026 | Hashmap lookup where in hashmap you can store the number and it's index so that once found you can return. This is not a two pointer one as it is not sorted |
| 167 | Two Sum II - Input Array Is Sorted | Medium | [Link](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | [Code](https://raw.githubusercontent.com/PHANINDRA-prog/dsa-april-2026/main/solutions/Array/2-two-sum-ii-input-array-is-sorted.py?raw=true) | May 17, 2026 | When array is sorted => Same number/duplicates are next to each other. Also check last and first with two pointers |
| 283 | Move Zeroes | Easy | [Link](https://leetcode.com/problems/move-zeroes/) | [Code](https://raw.githubusercontent.com/PHANINDRA-prog/dsa-april-2026/main/solutions/Array/8-move-zeroes.py?raw=true) | May 17, 2026 | Two pointers approach where one pointer is kept as start and if the element is non zero it will be swapped with supposing of insert_pos position  |
| 26 | Remove Duplicates from Sorted Array | Easy | [Link](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Code](https://raw.githubusercontent.com/PHANINDRA-prog/dsa-april-2026/main/solutions/Array/3-remove-duplicates-from-sorted-array.py?raw=true) | May 17, 2026 | Two pointers in same direction because it is sorted and also over here we put insert_pos and we find a element which is not matching there by unique element so we increment insert_pos or left and then replace it there by providing the solution |
| 238 | Product of Array Except Self | Medium | [Link](https://leetcode.com/problems/product-of-array-except-self/) | [Code](https://raw.githubusercontent.com/PHANINDRA-prog/dsa-april-2026/main/solutions/Array/4-product-of-array-except-self.py?raw=true) | May 23, 2026 | This is a prefix sum approach problem where we calculate the prefix multiplier for each index in prefix and post fix so that answer becomes prefix[i]*postfix[i] |
| 49 | Group Anagrams | Medium | [Link](https://leetcode.com/problems/group-anagrams/) | [Code](https://raw.githubusercontent.com/PHANINDRA-prog/dsa-april-2026/main/solutions/Array/9-group-anagrams.py?raw=true) | May 24, 2026 | Trick is to convert the element string into a ascii array count and then that becomes a common key for the words like eat and tea and there by we convert that list into tuple and then add it as a key and append elements who have matched that key |
