class Solution:
    def reverse(self, x: int) -> int:
        """
        x - int value
        return reverse but 32 bit
        """
        def isOverflow(n):
            if n > 2**31 or n < -2**31:
                return True
            else :
                return False
         
        old_digit_str = str(x)
        new_digit_str = ""
        old_digit_len = len(old_digit_str)
        positive = True if x >= 0 else False

        new_digit_str = old_digit_str[::-1]

        if not positive:
            new_digit_str = "-" + new_digit_str[:-1]

        new_digit_len = len(new_digit_str)

        # for letter in new_digit_str:
        #     if new_digit_str[0] == '0':
        #         new_digit_str = new_digit_str[1:len(new_digit_len)]
        #     else:
        #         break
        
        if isOverflow(int(new_digit_str)):
            return 0
        else :
            return int(new_digit_str)


x = Solution.reverse(None, -12300);

print(x);


# 2147483651
# 2147483648
# 4294967296