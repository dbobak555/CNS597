""" Dominic Bobak
    HW1 - Regular Expressions
    CNS 597
    3/31/2018
"""

##### Problem #####
##### CNS-380/597 - Ryan Haley####

import re

#Write a regular expression to fit the following:

#1 Phone number in the format of
#  xxx-xxx-xxxx
test1 = '123-123-1234'
regex1 = '\d{3}\-\d{3}\-\d{4}'
print(re.findall(regex1,test1))
#2 Phone number in the format of
#  (xxx) xxx-xxx
test2 = '(123) 123-1234'
regex2 = '\(\d{3}\)\ \d{3}\-\d{4}'
print(re.findall(regex2,test2))

#3 Phone number in the format of
#  +x xxx.xxx.xxxx
test3 = '+1 123.123.1234'
regex3 = '\+\d\ \d{3}\.\d{3}\.\d{4}'
print(re.findall(regex3,test3))

#4 SSN in the format of
#  xxx-xx-xxxx or xxxxxxxxx
test4 = '123-12-1234'
test5 = '123456789'
regex4 = '\d{3}\-\d{2}\-\d{4}|\d{9}'
print(re.findall(regex4,test4))
print(re.findall(regex4,test5))
