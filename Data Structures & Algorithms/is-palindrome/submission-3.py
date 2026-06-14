class Solution:
    def isPalindrome(self, s: str) -> bool:
        d = deque(c.lower() for c in s if c.isalnum())
        
        while len(d) > 1:
            # Compare and remove from both ends
            if d.popleft() != d.pop():
                return False
        
        return True

        