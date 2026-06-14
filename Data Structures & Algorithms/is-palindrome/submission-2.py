class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove everything that is not a letter or digit, lowercase it
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Compare string with its reverse
        return cleaned == cleaned[::-1]

        