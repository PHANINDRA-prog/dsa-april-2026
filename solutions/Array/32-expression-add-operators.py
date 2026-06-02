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