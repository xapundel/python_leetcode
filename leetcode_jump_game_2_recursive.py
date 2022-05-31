from typing import List

class Solution:
    def jump(self, nums: List[int], position = 0) -> int:
        # print("enter to position %d" % position)
        jumps = None
        finish = len(nums)
        if position +1 >= finish :
            return 0
        if (position + nums[position]+1 >= finish):
            # print("Reach %d" %position)
            return 1
        else :
            # print ((1, nums[position]))
            # jumps = 0
            for i in range(1, nums[position]+1) :
                # print("Jump from %d to %d" % (position, position+i));
                jumps_to_end = self.jump(nums, position+i)
                # print("Jump from %d to %d. Result %d" % (position, position+i, jumps_to_end));
   
                if jumps_to_end != None and (jumps == None or jumps_to_end < jumps) :
                    jumps = jumps_to_end
                
            # print("min jumps to the end from postion %d = %d" % ( position, jumps+1))
            return jumps +1 if jumps else None


s = Solution()
res = s.jump([2,3,1,1,4])
if res == None :
    print("No way")
elif res != 2:
    print ("Error 1. 2 != %d" %res)
else :
    print("Pass 1")


s = Solution()
res = s.jump([1,2,0,1], 0)
if res != 2:
    print ("Error 2. 2 != %d" %res)
else :
    print("Pass 2")

s = Solution()
res = s.jump([2,3,0,1,4], 0)
if res != 2:
    print ("Error 3. 2 != %d" %res)
else :
    print("Pass 3")