    
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    memo = {
        ')':'(',
        '}':'{',
        ']':'['
    }
        
    stack = []
        
    for i in s:
        if i in memo.values():
            stack.append(i)
        #check if the pop of the stack is the key of the value
        if i in memo.keys():
            if stack == []:
                return False
            elif stack.pop() != memo[i]:
                return False 
            else:
                continue 
                  
    if stack == []:
        return True 
    else:
        return False 