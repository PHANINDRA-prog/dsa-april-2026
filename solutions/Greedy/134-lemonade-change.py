class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:

        change_map = {5 : 0, 10: 0 , 20 : 0}


        for bill in bills:
            if bill == 5:
                change_map[5] += 1
            
            elif bill == 10:
                if change_map[5] > 0:
                    change_map[5] -= 1
                    change_map[10] += 1
                else:
                    return False
            
            elif bill == 20:
                if change_map[5] > 0 and change_map[10] > 0:
                    change_map[5] -= 1
                    change_map[10] -= 1
                elif change_map[5] >= 3:
                    change_map[5] -= 3
                else:
                    return False
        return True