def A(a:int):
    if a % 4 == 0:
        return False
    else:
        return True
    
# print(A(113))


def B(b:int):
    s = A(b)
    if s == True:
        return 
    else:
        t = [i for i in range(2, b) if i%4!=0]
        r = [i for  i in t if b%i==0 and i%2!=0].append(2)
        return r
    

# print(B(17))



class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
            # if i not in nums:
            a = []
            a.append(i)
            return a
            
a = Solution()
print(a.singleNumber([1,5,5]))
        