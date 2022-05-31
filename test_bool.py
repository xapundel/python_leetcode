
flag = True


for i in range(5):
    value = int(input());

    # if not(value % 10 == 0):
    #     flag = False;
    # the same as above
    flag = flag and value % 10 == 0;

print(flag)



