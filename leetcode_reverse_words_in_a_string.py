from operator import delitem


class Solution:
    def reverseWords(self, s: str) -> str:
        s_len = len(s)
        list_words = list()
        end_i = s_len
        # start_i = None
        is_letter = False
        for i in range(s_len-1, -1, -1):
            if s[i] == ' ' and is_letter:
                #store to list
                # print("store word:%s" % s[i+1:end_i+1])
                list_words.append(s[i+1:end_i+1])
                is_letter = False

            elif s[i] == ' ' and not is_letter :
                end_i = i
            else :
                # letter found
                if not is_letter:
                    end_i = i
                    is_letter = True
        else :
            if is_letter:
                list_words.append(s[0:end_i+1])
                
        return " ".join(list_words)
    



s = Solution()
result = s.reverseWords("the sky is blue")
if result != "blue is sky the":
    print ("Error 1. \"blue is sky the\" != \"%s\"" % result)
else :
    print ("Pass 1")