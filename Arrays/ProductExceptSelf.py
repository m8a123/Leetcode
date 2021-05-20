# def multiply_all(A):
#     if A == []:
#         return 1
#     return A[0]*multiply_all(A[1:])
    
class Solution(object):
    def productExceptSelf(self, A):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # if A == []:
        #     return 0
        # if len(A) == 2:
        #     return [A[1]]+[A[0]]
        #recurse for last element
        # ans = []
        # ans.append(multiply_all(A[1:]))
        #recurse for first element since it does not fit patter of A[0:i] + A[i+1:]
#         ans.append(multiply_all([A[0]]+A[2:]))
#         for i in range(2, len(A)-1):
#             ans.append(multiply_all(A[0:i] + A[i+1:]))

#         ans.append(multiply_all(A[:-1]))
#         return ans 
        left = [1]*len(A)
        right = [1]*len(A)
        ans = [1]*len(A)
        for i in range(1,len(A)):
            left[i] = A[i-1] * left[i-1]
        for i in range(len(A)-2, -1, -1):
            right[i] = A[i+1] * right[i+1]
        for i in range(len(A)):
            ans[i]= left[i]*right[i]
        return ans 