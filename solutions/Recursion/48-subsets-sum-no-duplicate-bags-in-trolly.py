nums = [1,2,2]
nums.sort()
def bottomhelper(index):
    if index == len(nums):
        return [0]
    
    answers = []
    childBag = bottomhelper(index+1)
    seen = set()

    for child in childBag:
        # Pick Case
        pick = child + nums[index]
        t1 = pick
        if t1 not in seen:
            seen.add(t1)
            answers.append(pick)
        # Not Pick Case
        t2 = (child)
        if t2 not in seen:
            seen.add(t2)
            answers.append(child)
    return answers
print( bottomhelper(0))



def tophelper(curr_sum,index):
    if index == len(nums):
        return [curr_sum]
    
    answers = []
    next_sum = curr_sum + nums[index]
    pick = tophelper(next_sum,index+1)
    answers.extend(pick)

    next_index = index + 1
    while next_index < len(nums) and nums[next_index] == nums[index]:
        next_index += 1
    
    next_sum = curr_sum
    notPick = tophelper(next_sum,next_index)
    answers.extend(notPick)
    return answers
print (tophelper(0,0))


















