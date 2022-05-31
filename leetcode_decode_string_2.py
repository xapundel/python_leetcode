from tracemalloc import start


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for e in s:
            if e == "]":
                word = ""
                while stack and stack[-1] != "[":
                    word = stack.pop() + word
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * word)
            else: 
                stack.append(e)
                
        return "".join(stack) 





s = Solution()
res = s.decodeString("13[a]2[bc]")
if res != "aaaaaaaaaaaaabcbc":
    print ("Error 1. aaaaaaaaaaaaabcbc != %s" %res)
else :
    print("Pass 1")

res = s.decodeString("3[a2[c]]")
if res != "accaccacc":
    print ("Error 1. accaccacc != %s" %res)
else :
    print("Pass 1")
    

res = s.decodeString("2[abc]3[cd]ef")
if res != "abcabccdcdcdef":
    print ("Error 1. abcabccdcdcdef != %s" %res)
else :
    print("Pass 1")

