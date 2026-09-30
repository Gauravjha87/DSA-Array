class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        low = min(bloomDay)
        high = max(bloomDay)
        

        if(m * k > n):
            return -1
        
        while low < high:

            mid = low + (high - low) // 2

            bouquets = 0
            flowers = 0

            for bloom in bloomDay:

                if bloom <= mid:
                    flowers += 1

                    if flowers == k:
                        bouquets += 1
                        flowers = 0

                else:
                    flowers = 0

            if bouquets >= m:
                high = mid
            else:
                low = mid + 1

        return low
        
        
        