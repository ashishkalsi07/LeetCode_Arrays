class Solution(object):
    def sortPeople(self, names, heights):
        pairs = list(zip(names, heights))
        sorted_pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        sorted_names = [pair[0] for pair in sorted_pairs]
        print(sorted_names)


S = Solution()
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
S.sortPeople(names, heights)
