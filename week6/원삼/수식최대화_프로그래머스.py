from itertools import permutations
def solution(expression):
    nums = []
    exp = []
    answer = []
    n_ = ""
    for i in expression:
        try:
            int(i)
            n_ += i
        except:
            nums.append(int(n_))
            n_ = ""
            nums.append(i)
            exp.append(i)
    nums.append(int(n_))
    exp = set(exp)
    
    exp_list = [i for i in permutations(exp,len(exp))]
    for i in exp_list:
        nums_ = nums
        for x in i:
            if x == "*":
                nums_ = multi(nums_)
            elif x == "+":
                nums_ = plus(nums_)               
            else:
                nums_ = minus(nums_)
        answer.append(abs(int(nums_[0])))
        
    return max(answer)
                
def multi(nums):
    ans = []
    passing = False
    for i in range(len(nums)):
        if nums[i] == "*":
            x = ans.pop()
            ans.append(x * nums[i+1])
            passing = True
        elif passing == True:
            passing = False
            pass
        else:
            ans.append(nums[i])
    return ans

def plus(nums):
    ans = []
    passing = False
    for i in range(len(nums)):
        if nums[i] == "+":
            x = ans.pop()
            ans.append(x + nums[i+1])
            passing = True
        elif passing == True:
            passing = False
            pass
        else:
            ans.append(nums[i])
    return ans

def minus(nums):
    ans = []
    passing = False
    for i in range(len(nums)):
        if nums[i] == "-":
            x = ans.pop()
            ans.append(x - nums[i+1])
            passing = True
        elif passing == True:
            passing = False
            pass
        else:
            ans.append(nums[i])
    return ans