class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for f in range(len(flowerbed)):
            if not flowerbed[f]:
                if f+2 < len(flowerbed):
                    if not flowerbed[f+2]:
                        n-=1
        if n > 0:
            return False
        return True


flowerbed = [1,0,0,0,1]
n = 2
print(Solution().canPlaceFlowers(flowerbed = flowerbed, n = n))