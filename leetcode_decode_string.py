from tracemalloc import start


class Solution:
    def decodeString(self, s: str) -> str:
        # resulted_str = ""
        number = ""
        while True:
            start_i = 0
            end_i = 0
            i = 0
            for l in s:
                if l == '[':
                    start_i = i
                if l == ']':
                    end_i = i
                    break;
                i += 1

            # print("start index:\t%d \nend_index:\t%d \n" %(start_i, end_i))
            
            if start_i != 0:
                digit = self.get_digit(s, start_i)
                digit_len = len(str(digit))
                head = s[0:start_i]
                head = head[0:-digit_len]
                tail = s[end_i+1:]
                body = self.multiply(s[start_i+1:end_i], digit)
                # print("head:\t%s \nbody:\t%s \ntail:\t%s \n" %(head, body, tail))

                s = head + body + tail
            else :
                 break
        # print("resulted string :\t %s" % s)
        return s




    def multiply (self, s, digit):
        res_str = ""
        for i in range(digit):
            res_str += s
        return res_str


    def get_digit(self, s , start_i) :
        mult = 1
        result = 0
        for i in range (start_i-1, -1, -1 ):
            # print("->"+s[i])
            if s[i].isdigit() :
                
                result += int(s[i]) * mult
                mult *= 10
            else :
                break
        # print("->>" + str(result))
        return result





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

