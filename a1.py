import re

text = "A1-A2-A3-A4-B1-A5-A6-A7-A8"
matches = re.findall(r"(A\d)-A\d",text))
for match in matches: