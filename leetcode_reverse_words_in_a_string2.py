from operator import delitem


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join((s.split())[::-1])
    



s = Solution()
result = s.reverseWords("the sky is blue")
if result != "blue is sky the":
    print ("Error 1. \"blue is sky the\" != \"%s\"" % result)
else :
    print ("Pass 1")