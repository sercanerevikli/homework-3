def rev_string(input):
    str = ""
    for i in input:
        str = i + str
    return str


s=input("Please type someting here to reverse : ")

rmv_space=s.replace(" ", "")

lower_string=rmv_space.lower()
rev_string_display=rev_string(lower_string)
print(rev_string_display)

import sys
sys.exit(0)