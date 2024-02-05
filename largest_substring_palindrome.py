class Solution:
    def longestPalindrome(self, s: str) -> str:

        # Solution Expand from center

        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str

        # Solution 1 O(n^2)
        
        m = 0
        ans = ''

        def isPalindrome(string):
            print(string, string[::-1])
            return string == string[::-1]

        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(s[i: j+1]):
                    temp = max(m, len(s[i: j+1]))
                    if temp > m:
                        m = temp
                        ans = s[i: j+1]
        return ans

