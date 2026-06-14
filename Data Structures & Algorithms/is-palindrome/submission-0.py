class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric chars
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            # Compare chars case-insensitively
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
    
        return True




        