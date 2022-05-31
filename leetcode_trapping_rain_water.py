from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        h_len = len(height)
        dp = [None] * h_len
        max_left = 0
        counter = 0
        for i in height :
            dp[counter] = max_left
            max_left = i if max_left < i else max_left

            counter += 1

        counter = h_len-1
        max_right = 0

        result = 0
        for i in range(h_len-1, -1, -1) :
            dp[counter] = min(dp[counter],max_right)
            max_right = height[i] if max_right < height[i] else max_right

            tmp_res = dp[counter] - height[i]
            tmp_res = tmp_res if tmp_res > 0 else 0
            result += tmp_res

            counter -= 1

        return result



s = Solution()
result = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
if result != 6:
    print ("Error 1. 6 != \"%d\"" % result)
else :
    print ("Pass 1")


s = Solution()
result = s.trap([4,2,0,3,2,5])
if result != 9:
    print ("Error 2. 9 != \"%d\"" % result)
else :
    print ("Pass 2")