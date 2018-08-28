import re  # regular expressions

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()
last_name = r"Love"
first_name = r"Kenneth"
# print(re.match(last_name, data))
# print(re.search(first_name, data))
# print(re.findall(r"\(?\d{3}\)? \d{3}-\d{4}", data))
# print(re.findall(r"\w*, \w+", data))
# Fur email
# print(re.findall(r"\b[trehous]{9}\b", data, re.I))
# print(re.findall(r"[-\w\d+.]+@[-\w\d.]+",data))
# with exclusions
# print(re.findall(r"" "\n"
#                  r"    \b@[-\w\d.]* #word boundary, @ and any number of characters" "\n"
#                  r"    [^gov\t]+  #ignore 1+ instances of letters g o v and a tab" "\n"
#                  r"    \b  #match word boundart" "\n"
#                  r"    ", data, re.VERBOSE | re.I))
#verbose ex
# print(re.findall(r"" "\n"
#                  r'                 \b[-\w]*,   #find a word boundary, 1+ hyphens or charaters and a comma"' "\n"
#                  r'                 \s  #find 1 whitespace"' "\n"
#                  r'                 [-\w ]+  #find 1+hyphens and characters and explicit spaces"' "\n"
#                  r'                 [^\t\n] #ignore tabs and newlines"' "\n"
#                  r"                 ", data, re.X))

line = re.search(r"" "\n"
                 r"    ^(?P<name>[-\w ]*,\s[-\w ]+)\t   #Last and first names" "\n"
                 r"    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email" "\n"
                 r"    (?P<phone>\(?\d{3}\)?.?\s?\d {3}-\d{4})?\t    #phone" "\n"
                 r"    (?P<work>[\w\s]+,\s[\w\s.]+)\t?   #job and company" "\n"
                 r"    (?P<twitter>@[\w\d]+)?$  #Twitter" "\n"
                 r"    ", data, re.X | re.MULTILINE)

print(line)
print(line.groupdict())