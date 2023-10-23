#!/usr/bin/env python3

import sys
import urllib.parse as ul

# print either the argument or stdin and parse and urldecode
if sys.argv[1]:
    print(ul.unquote_plus(sys.argv[1]))
else:
    print(ul.unquote_plus(sys.stdin.read()))
