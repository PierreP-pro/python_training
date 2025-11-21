"""
import time

phrase = "I don't know, but it seems cloudy today."

finded = phrase.find("do")

print(finded)

print("do" in phrase)


print(time.time())
"""

import re


zip_code = r"\d{5}"

search = re.search(zip_code, "Beverly Hills 90210")

if search:
    print("It's got a ZIP code!")
else:
    print("No match!")



print(search)
