class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "" :
            return 0
        dict = {}
        result = 0
        maximum = 0
        index = 0
        zero_index = 0
        for i in s:
            if i in dict:
                result = result - (dict[i] - zero_index)
                zero_index = dict[i] + 1
                dict = {key:val for key, val in dict.items() if val >= dict[i]}
                dict[i] = index
                if result < 1 :
                    result = 1 
            else :
                result += 1
                if result > maximum : maximum = result
                dict[i] = index
            index += 1
        return maximum
        
s = Solution()
res = s.lengthOfLongestSubstring("abcabcbb")
if res != 3:
    print ("Error 1. 3 != %d" %res)
else :
    print("Pass 1")

s = Solution()
res = s.lengthOfLongestSubstring("bbbbb")
if res != 1:
    print ("Error 2. 1 != %d" %res)
else :
    print("Pass 2")

s = Solution()
res = s.lengthOfLongestSubstring("pwwkew")
if res != 3:
    print ("Error 3. 3 != %d" %res)
else :
    print("Pass 3")


s = Solution()
res = s.lengthOfLongestSubstring("aab")
if res != 2:
    print ("Error 4. 2 != %d" %res)
else :
    print("Pass 4")

s = Solution()
res = s.lengthOfLongestSubstring("dvdf")
if res != 3:
    print ("Error 5. 3 != %d" %res)
else :
    print("Pass 5")


s = Solution()
res = s.lengthOfLongestSubstring("abac")
if res != 3:
    print ("Error 6. 3 != %d" %res)
else :
    print("Pass 6")

s = Solution()
res = s.lengthOfLongestSubstring("tmmzuxt")
if res != 5:
    print ("Error 7. 5 != %d" %res)
else :
    print("Pass 7")

s = Solution()
res = s.lengthOfLongestSubstring("bbtablud")
if res != 6:
    print ("Error 8. 6 != %d" %res)
else :
    print("Pass 8")