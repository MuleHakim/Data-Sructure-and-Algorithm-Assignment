# This is a program which evaluate a postfix expression

import re
import math
def award200(Oper):
    # I split the strings using comma
    Oper = Oper.split(",")
    stack1 = []
    for i in range(len(Oper)):
        # I used isdigit() to check if the string is digit
        # I used re.match to handle if the number is negative
        if Oper[i].isdigit() or re.match("(-\w)",Oper[i]):
            stack1.append(int(Oper[i]))
        else:
            if Oper[i]=="+":
                a = stack1.pop()
                b = stack1.pop()
                stack1.append(b+a)
            elif Oper[i]=="*":
                a = stack1.pop()
                b = stack1.pop()
                stack1.append(b*a)
            elif Oper[i]=="-":
                a = stack1.pop()
                b = stack1.pop()
                stack1.append(b-a)
            else:
                # this is for division ("/")
                a = stack1.pop()
                b = stack1.pop()
                if (a < 0 and b > 0) or ( a > 0 and b < 0):
                    stack1.append(math.ceil(b/a))
                else:
                    stack1.append(b//a)
    return stack1.pop()
    

print("The answer will be :", award200("5,8,16,/,2,2,*,-,+"))       #  1
print("The answer will be :", award200("-2,8,*,3,7,/,2,4,*,-,+"))   #  -24
print("The answer will be :", award200("15,5,/,2,11,*,20,-,+"))     #  5 