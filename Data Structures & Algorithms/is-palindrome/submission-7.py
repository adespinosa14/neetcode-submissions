class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1

        s = s.lower()

        while front <= back:

            if s[front].isalpha() == False and s[front].isdigit() == False:
                front += 1
                continue

            if s[back].isalpha() == False and s[back].isdigit() == False:
                back -= 1
                continue

            if s[front] != s[back]: 
                return False
            front += 1
            back -= 1
        
        return True
        