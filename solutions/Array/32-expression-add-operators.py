// TC : O(2^n)
// SC : O(n)
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        result = []

        def backtrack(index, expression, total, previous):

            # Base Case
            if index == len(num):

                if total == target:
                    result.append(expression)

                return


            # Partition next number
            for end in range(index, len(num)):

                current = num[index:end + 1]

                # Prevent leading zeros
                if len(current) > 1 and current[0] == "0":
                    break

                value = int(current)


                # First number → no operator
                if index == 0:

                    backtrack(
                        end + 1,
                        current,
                        value,
                        value
                    )

                else:

                    # +
                    backtrack(
                        end + 1,
                        expression + "+" + current,
                        total + value,
                        value
                    )

                    # -
                    backtrack(
                        end + 1,
                        expression + "-" + current,
                        total - value,
                        -value
                    )

                    # *
                    backtrack(
                        end + 1,
                        expression + "*" + current,
                        total - previous + (previous * value),
                        previous * value
                    )


        backtrack(
            0,
            "",
            0,
            0
        )

        return result





# Much Better partition solution
from typing import List

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []
        
        # path: the expression string built so far
        # total: the running mathematical total of 'path'
        # prev_num: memory of the last individual number added/subtracted
        def backtrack(index, path, total, prev_num):
            # 1. Base Case: If we have partitioned the entire string of digits
            if index == len(num):
                if total == target:
                    result.append(path)
                return
            
            # 2. The Core Partitioning Loop
            for i in range(index, len(num)):
                
                # Edge Case: Prevent numbers with leading zeros (e.g., "05" is invalid, "0" is fine)
                if i > index and num[index] == '0':
                    break
                
                # Slice the chunk out and turn it into an integer
                part_str = num[index : i + 1]
                val = int(part_str)
                
                # 3. Position 0: The very first number has no operator behind it
                if index == 0:
                    # Total is val, and our last touched number (memory) is also val
                    backtrack(i + 1, part_str, val, val)
                else:
                    # Choice A: Add '+' operator
                    # New string copy is made implicitly, total increases, memory is positive val
                    backtrack(i + 1, path + "+" + part_str, total + val, val)
                    
                    # Choice B: Add '-' operator
                    # New string copy is made implicitly, total decreases, memory is negative val
                    backtrack(i + 1, path + "-" + part_str, total - val, -val)
                    
                    # Choice C: Add '*' operator
                    # Roll back the previous number from total, multiply it, and add it back
                    # New memory becomes (prev_num * val)
                    backtrack(i + 1, path + "*" + part_str, (total - prev_num) + (prev_num * val), prev_num * val)

        # Start the recursion at index 0 with an empty string, total 0, and memory 0
        backtrack(0, "", 0, 0)
        return result
