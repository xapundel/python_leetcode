from typing import List

class Solution:
    def jump(self, nums: List[int], position = 0, dp = None) -> int:
        if dp == None :
            dp = {}
        jumps = None
        finish = len(nums)
        if position +1 >= finish :
            dp[position] = 0
            print("yep")
            return 0
        if (position + nums[position]+1 >= finish):
            dp[position] = 1
            return 1
        else :
            for i in range(1, nums[position]+1) :
                if position + i in dp :
                    jumps_to_end = dp[position + i]
                else :  
                    jumps_to_end = self.jump(nums, position+i, dp)
   
                if jumps_to_end != None and (jumps == None or jumps_to_end < jumps) :
                    jumps = jumps_to_end
            if jumps != None :
                dp[position] = jumps + 1    
            return jumps +1 if jumps else None


# s = Solution()
# res = s.jump([2,3,1,1,4])
# if res == None :
#     print("No way")
# elif res != 2:
#     print ("Error 1. 2 != %d" %res)
# else :
#     print("Pass 1")


# s = Solution()
# res = s.jump([0], 0)
# if res != 0:
#     print ("Error 2. 2 != %d" %res)
# else :
#     print("Pass 2")

# s = Solution()
# res = s.jump([1,2,0,1], 0)
# if res != 2:
#     print ("Error 2. 2 != %d" %res)
# else :
#     print("Pass 2")

s1 = Solution()
res1 = s1.jump([2,3,0,1,4], 0)
if res1 != 2:
    print ("Error 3. 2 != %d" %res1)
else :
    print("Pass 3")

s = Solution()
res = s.jump([1,1,1,1], 0)
if res != 3:
    print ("Error 4. 3 != %d" %res)
else :
    print("Pass 4")