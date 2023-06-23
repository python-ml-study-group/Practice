import re
str1="$1499"
newstr1=re.sub(r'[$]','',str1).strip()
print(newstr1)