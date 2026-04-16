class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l,r = l+1,r-1
            return True
            
        
        out = []
        curr = []
        n = len(s)

        def backtrack(index):
            if index == n:
                out.append(curr[:])
                return
            
            for i in range(index,n):
                if is_palindrome(s,index,i):
                    curr.append(s[index:i+1])
                    backtrack(i+1)
                    curr.pop()
        
        backtrack(0)
        return out
