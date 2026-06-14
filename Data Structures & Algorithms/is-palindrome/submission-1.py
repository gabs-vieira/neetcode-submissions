class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean: keep only alphanumeric chars, lowercase
        cleaned = [c.lower() for c in s if c.isalnum()]
        n = len(cleaned)
        
        # Only need to check the first half against the mirrored second half
        for i in range(n // 2):
            if cleaned[i] != cleaned[n - 1 - i]:
                return False
        
        return True
    