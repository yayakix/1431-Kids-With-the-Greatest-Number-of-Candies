class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max = 0
        ans = []
        for i in range(len(candies)):
            if candies[i] > max:
                max = candies[i]
        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= max)
        return ans
