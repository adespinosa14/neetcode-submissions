class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''.join(char for char in s if char.isalpha() or char.isdigit()).lower()

        left = 0
        right = len(new_str) - 1

        print(new_str)

        while True:
            if right <= left: break
            if new_str[left] != new_str[right]: return False

            left += 1
            right -= 1


        return True
        