#!/usr/bin/python [Created By Mandeep]

from urllib2 import *

import sys 

url = input("Enter the Full Url Of The Target Website : ")
url.rstrip()
header=urllib2.urlopen(url).info()
print(str(header))
