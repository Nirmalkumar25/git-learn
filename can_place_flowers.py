class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        '''
        canPlace = 0
        position = 0
        while position < len(flowerbed):
            pre_position = position - 1
            post_position = position + 1 
            if flowerbed[position] == 0 and (flowerbed[pre_position] and flowerbed[post_position == 0]):
                canPlace+=1
            position +=1
        if canPlace == n:
            return True
        return False
        '''
        canplace = 0
        position = 0
        while position < len(flowerbed):
            if flowerbed[position]:
                position+=2
            else:
                post_position = position + 1
                pre_position = position - 1
                if pre_position < 0: pre_position = 0
                if post_position >= len(flowerbed): post_position = len(flowerbed)-1
                if (position == 0 and flowerbed[post_position] == 0) or (position == len(flowerbed)-1 and flowerbed[pre_position] == 0) or (flowerbed[pre_position] == 0 and flowerbed[post_position] == 0):
                    canplace+=1
                    flowerbed[position] = 1
                position+=1
        return canplace >= n
    
flowerbed = [0,0,1,0,0]
n = 1
print(Solution().canPlaceFlowers(flowerbed = flowerbed, n = n))