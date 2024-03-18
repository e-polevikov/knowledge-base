class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        nrows, ncols = len(s) + 1, len(p) + 1

        matches = [[False for _ in range(ncols)] for _ in range(nrows)]

        matches[0][0] = True
        
        for i in range(1, nrows):
            for j in range(1, ncols):
                if (s[i - 1] == p[j - 1] or p[j - 1] == ".") and matches[i - 1][j - 1]:
                    matches[i][j] = True
                elif p[j - 1] == "*":
                    matches[i][j] = True
                
        return matches[-1][-1]

        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isMatch("aab", "*ba"))
