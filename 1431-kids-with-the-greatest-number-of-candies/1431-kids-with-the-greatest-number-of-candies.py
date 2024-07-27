class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        stand = max(candies) - extraCandies
        for i in range(len(candies)):
            if candies[i] < stand:
                candies[i] = False
            else:
                candies[i] = True  

        return candies


        