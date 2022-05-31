class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0": 
            return "0"
        result = 0
        mult2 = 1
        for l_num2 in range(len(num2)-1, -1, -1):
            mult1 = 1
            tmp_res = 0
            for l_num1 in range(len(num1)-1, -1, -1):
                simple_mult =int(num2[l_num2]) * int(num1[l_num1])
                tmp_res = tmp_res +simple_mult * mult1 * mult2
                mult1 *=10
            result += tmp_res
            mult2 *= 10
        return str(result)



s = Solution()
res = s.multiply("123", "456")
if res != "56088":
    print ("Error 1, 56088 != %s " % res)
else :
    print ("Pass 1")

res = s.multiply("0", "0")
if res != "0":
    print ("Error 2, 0 != %s " % res)
else :
    print ("Pass 2")

res = s.multiply("2", "3")
if res != "6":
    print ("Error 3, 6 != %s" % res)
else :
    print ("Pass 3")