class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = []
        for i in range(len(candies)):
            popped = candies.pop(i)
            has = popped+extraCandies
            for j in candies:
                greatest = True
                if has < j:
                    greatest = False
                    break
            res.append(greatest)
            candies.insert(i,popped)
        return res

candies = [4,2,1,1,2]
extraCandies = 1
print(Solution().kidsWithCandies(candies=candies, extraCandies=extraCandies))

