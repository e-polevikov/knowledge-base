class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """

        prefix_distinct_letters = [0] * len(s)
        suffix_distinct_letters = [0] * len(s)

        prefix_distinct_letters_set = set()
        suffix_distinct_letters_set = set()

        for i in range(len(s)):
            prefix_distinct_letters_set.add(s[i])
            suffix_distinct_letters_set.add(s[len(s) - i - 1])

            prefix_distinct_letters[i] = len(prefix_distinct_letters_set)
            suffix_distinct_letters[len(s) - i - 1] = len(suffix_distinct_letters_set)
        
        num_splits = 0

        for i in range(len(s) - 1):
            if prefix_distinct_letters[i] == suffix_distinct_letters[i + 1]:
                num_splits += 1
        
        return num_splits


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSplits("aabaab"))
