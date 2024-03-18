class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        cache = [[None for _ in range(len(s))] for _ in range(len(s))]

        def isPalindrome(s, i, j):
            if cache[i][j] is not None:
                return cache[i][j]

            if i == j:
                cache[i][j] = True
            elif i == j - 1:
                cache[i][j] = s[i] == s[j]
            elif s[i] != s[j]:
                cache[i][j] = False
            else:
                cache[i][j] = isPalindrome(s, i + 1, j - 1)
            
            return cache[i][j]
        
        pbegin, pend = 0, 0

        for k in range(1, len(s) + 1):
            for i in range(len(s) - k):
                if isPalindrome(s, i, i + k):
                    if k > pend - pbegin:
                        pbegin, pend = i, i + k

        return s[pbegin : pend + 1]


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("cbbd"))
