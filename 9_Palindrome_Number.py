class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        result = 0
        origin = x
        while x>0:
            result = 10*result + x%10
            x=x//10
        return origin==result
        
        